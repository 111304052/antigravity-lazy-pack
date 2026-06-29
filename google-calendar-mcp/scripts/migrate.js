import fs from 'fs/promises';
import path from 'path';
import { google } from 'googleapis';
import { OAuth2Client } from 'google-auth-library';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const sourceCalendarId = '111304052@g.nccu.edu.tw';
const destinationCalendarId = 'primary';

// Helper function to add delay between API calls to prevent rate limiting
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function main() {
  const keysPath = path.join(__dirname, '../gcp-oauth.keys.json');
  const tokensPath = path.join(__dirname, '../.gcp-saved-tokens.json');

  const keys = JSON.parse(await fs.readFile(keysPath, 'utf-8'));
  const tokens = JSON.parse(await fs.readFile(tokensPath, 'utf-8'));

  const { client_id, client_secret, redirect_uris } = keys.installed;
  const oauth2Client = new OAuth2Client({
    clientId: client_id,
    clientSecret: client_secret,
    redirectUri: redirect_uris[0]
  });
  oauth2Client.setCredentials(tokens);

  const calendar = google.calendar({ version: 'v3', auth: oauth2Client });

  // Time range for migration (2026 to 2027)
  const timeMin = '2026-01-01T00:00:00Z';
  const timeMax = '2027-12-31T23:59:59Z';

  console.log(`\n=== Starting Google Calendar Migration ===`);
  console.log(`Source: ${sourceCalendarId}`);
  console.log(`Destination: ${destinationCalendarId}`);
  console.log(`Time Range: ${timeMin} to ${timeMax}\n`);

  // 1. Fetch destination events (to identify duplicates)
  console.log('Fetching existing events from destination calendar...');
  const destEvents = [];
  let destPageToken = undefined;
  do {
    const res = await calendar.events.list({
      calendarId: destinationCalendarId,
      timeMin: timeMin,
      timeMax: timeMax,
      singleEvents: true,
      maxResults: 250,
      pageToken: destPageToken,
    });
    if (res.data.items) {
      destEvents.push(...res.data.items);
    }
    destPageToken = res.data.nextPageToken;
    await delay(100); // polite delay
  } while (destPageToken);

  console.log(`-> Found ${destEvents.length} existing events in destination calendar.\n`);

  // Map of existing events: key = "summary_startTime" -> eventId
  const existingMap = new Map();
  for (const event of destEvents) {
    const startStr = event.start?.dateTime || event.start?.date || '';
    const key = `${event.summary || 'Untitled'}_${startStr}`;
    existingMap.set(key, event.id);
  }

  // 2. Fetch source events from the school calendar
  console.log('Fetching events from source (school) calendar...');
  const sourceEvents = [];
  let sourcePageToken = undefined;
  do {
    const res = await calendar.events.list({
      calendarId: sourceCalendarId,
      timeMin: timeMin,
      timeMax: timeMax,
      singleEvents: true,
      maxResults: 250,
      pageToken: sourcePageToken,
    });
    if (res.data.items) {
      sourceEvents.push(...res.data.items);
    }
    sourcePageToken = res.data.nextPageToken;
    await delay(100); // polite delay
  } while (sourcePageToken);

  console.log(`-> Found ${sourceEvents.length} events in source (school) calendar.\n`);

  // 3. Migrate events
  let copiedCount = 0;
  let replacedCount = 0;
  let errorCount = 0;

  for (const event of sourceEvents) {
    try {
      const startStr = event.start?.dateTime || event.start?.date || '';
      const key = `${event.summary || 'Untitled'}_${startStr}`;

      // Check if duplicate exists
      if (existingMap.has(key)) {
        const existingEventId = existingMap.get(key);
        console.log(`[REPLACE] Duplicate found: "${event.summary}" (${startStr}). Deleting old ICS import...`);
        
        await calendar.events.delete({
          calendarId: destinationCalendarId,
          eventId: existingEventId,
        });
        
        replacedCount++;
        await delay(150); // delay after delete
      } else {
        console.log(`[CREATE] Copying new event: "${event.summary}" (${startStr})`);
        copiedCount++;
      }

      // Insert new event with original settings (colorId, reminders, etc.)
      const newEvent = {
        summary: event.summary,
        description: event.description,
        location: event.location,
        start: event.start,
        end: event.end,
        colorId: event.colorId,
        reminders: event.reminders,
        recurrence: event.recurrence, // just in case, though singleEvents is true
      };

      await calendar.events.insert({
        calendarId: destinationCalendarId,
        requestBody: newEvent,
      });

      await delay(150); // delay after insert to respect rate limits
    } catch (err) {
      console.error(`[ERROR] Failed to migrate event "${event.summary}":`, err.message);
      errorCount++;
    }
  }

  console.log(`\n=== Migration Completed ===`);
  console.log(`- Created new: ${copiedCount}`);
  console.log(`- Overwritten/Replaced: ${replacedCount}`);
  console.log(`- Errors encountered: ${errorCount}`);
  console.log(`===========================`);
}

main().catch(console.error);
