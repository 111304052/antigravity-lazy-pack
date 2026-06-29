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

function getColorId(summary) {
  if (!summary) return null;
  const s = summary.toLowerCase();
  
  // 截止日、重要事項 - 紅色 ('11')
  if (s.includes('截止') || s.includes('重要') || s.includes('deadline')) {
    return '11';
  }
  
  // 講座 - 黃色 ('5')
  if (s.includes('講座') || s.includes('研討會')) {
    return '5';
  }
  
  // 打球、運動、比賽(盃賽)、重訓 - 藍色 ('7')
  if (s.includes('打球') || s.includes('運動') || s.includes('比賽') || s.includes('盃賽') || s.includes('重訓') || s.includes('練球') || s.includes('匹克球') || s.includes('球敘') || s.includes('社會團') || s.includes('個人賽') || s.includes('球拍') || s.includes('體育館')) {
    return '7';
  }
  
  // 休閒活動(逛街、買東西、看電影、看醫生、咖啡廳) - 綠色 ('10')
  if (s.includes('逛街') || s.includes('買東西') || s.includes('看電影') || s.includes('看醫生') || s.includes('咖啡廳') || s.includes('逛') || s.includes('三井') || s.includes('電影') || s.includes('美麗華') || s.includes('皮膚科') || s.includes('修修臉')) {
    return '10';
  }
  
  // 學業(上課、科目、考試) - 紫色 ('3')
  if (s.includes('上課') || s.includes('考試') || s.includes('期末考') || s.includes('期末準備') || s.includes('離散數學') || s.includes('隨機過程') || s.includes('統計機器學習') || s.includes('工程數學') || s.includes('等候理論') || s.includes('自主學習') || s.includes('課程') || s.includes('python') || s.includes('認證')) {
    return '3';
  }
  
  // 吃飯、交通、雜務 - 灰色 ('8')
  if (s.includes('吃飯') || s.includes('交通') || s.includes('雜務') || s.includes('晚餐') || s.includes('吃豆花') || s.includes('餐酒館') || s.includes('回台北') || s.includes('回政大') || s.includes('往宜蘭') || s.includes('自強') || s.includes('繳費') || s.includes('洗面乳') || s.includes('畢業證書') || s.includes('申請離校') || s.includes('橘子') || s.includes('冠金華') || s.includes('麵食主義') || s.includes('食義') || s.includes('吃') || s.includes('飯') || s.includes('車次')) {
    return '8';
  }
  
  return null; // default
}

function getEventKey(summary, startObj) {
  if (!startObj) return `${summary || 'Untitled'}_`;
  
  let startStr = '';
  if (startObj.date) {
    startStr = startObj.date; // YYYY-MM-DD
  } else if (startObj.dateTime) {
    // Normalize timezone offsets to UTC ISO string
    startStr = new Date(startObj.dateTime).toISOString();
  }
  return `${summary || 'Untitled'}_${startStr}`;
}

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

  console.log(`\n=== Starting Google Calendar API Migration ===`);
  console.log(`Source shared calendar: ${sourceCalendarId}`);
  console.log(`Destination: ${destinationCalendarId}`);
  console.log(`Time Range: ${timeMin} to ${timeMax}\n`);

  // 1. Fetch destination events (to identify and remove duplicates/ICS files)
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
    await delay(100);
  } while (destPageToken);

  console.log(`-> Found ${destEvents.length} existing events in destination calendar.\n`);

  // Map of existing events: key = "summary_startTime" -> Array of eventIds
  const existingMap = new Map();
  for (const event of destEvents) {
    const key = getEventKey(event.summary, event.start);
    if (!existingMap.has(key)) {
      existingMap.set(key, []);
    }
    existingMap.get(key).push(event.id);
  }

  // 2. Fetch source events from the shared school calendar (expanded recurring events)
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
    await delay(100);
  } while (sourcePageToken);

  console.log(`-> Found ${sourceEvents.length} events in source (school) calendar.\n`);

  // 3. Migrate events
  let copiedCount = 0;
  let replacedCount = 0;
  let errorCount = 0;

  for (const event of sourceEvents) {
    try {
      const key = getEventKey(event.summary, event.start);
      const startStr = event.start?.dateTime || event.start?.date || '';

      // Check if duplicate exists (could be multiple duplicates from prior attempts)
      if (existingMap.has(key)) {
        const existingEventIds = existingMap.get(key);
        console.log(`[REPLACE] Duplicate found: "${event.summary}" (${startStr}). Deleting ${existingEventIds.length} old event(s)...`);
        
        for (const existingEventId of existingEventIds) {
          await calendar.events.delete({
            calendarId: destinationCalendarId,
            eventId: existingEventId,
          });
          await delay(150);
        }
        
        replacedCount++;
      } else {
        console.log(`[CREATE] Copying new event from school calendar: "${event.summary}" (${startStr})`);
        copiedCount++;
      }

      // Map colorId based on user rules
      const colorId = getColorId(event.summary);

      // Prepare event resource body, copying reminders directly
      const newEvent = {
        summary: event.summary,
        description: event.description,
        location: event.location,
        start: event.start,
        end: event.end,
        colorId: colorId,
        reminders: event.reminders, // copy reminders (useDefault or overrides)
      };

      await calendar.events.insert({
        calendarId: destinationCalendarId,
        requestBody: newEvent,
      });

      await delay(150); // respect rate limits
    } catch (err) {
      console.error(`[ERROR] Failed to migrate event "${event.summary}":`, err.message);
      errorCount++;
    }
  }

  console.log(`\n=== API Migration Completed ===`);
  console.log(`- Created new: ${copiedCount}`);
  console.log(`- Overwritten/Replaced: ${replacedCount}`);
  console.log(`- Errors encountered: ${errorCount}`);
  console.log(`===========================`);
}

main().catch(console.error);
