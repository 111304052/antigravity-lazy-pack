const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const PORT = 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');
const DATA_FILE = path.join(__dirname, 'data', 'ledger.json');
const OBSIDIAN_VAULT = 'C:\\Users\\leots\\OneDrive\\文件\\Secondbrain';

// Ensure data folder and file exist
const dataDir = path.dirname(DATA_FILE);
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}
if (!fs.existsSync(DATA_FILE)) {
  const initialData = {
    transactions: [],
    accounts: [
      { id: 'cash', name: '現金', balance: 0 },
      { id: 'bank', name: '銀行', balance: 0 },
      { id: 'card', name: '信用卡', balance: 0 }
    ]
  };
  fs.writeFileSync(DATA_FILE, JSON.stringify(initialData, null, 2), 'utf8');
}

// Helper to get local IP
function getLocalIPs() {
  const interfaces = os.networkInterfaces();
  const addresses = [];
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      if (iface.family === 'IPv4' && !iface.internal) {
        addresses.push(iface.address);
      }
    }
  }
  return addresses;
}

// MIME types for static files
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // 1. API: Get ledger data
  if (req.method === 'GET' && pathname === '/api/data') {
    fs.readFile(DATA_FILE, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Failed to read data file' }));
        return;
      }
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(data);
    });
    return;
  }

  // 2. API: Save ledger data
  if (req.method === 'POST' && pathname === '/api/save') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        fs.writeFile(DATA_FILE, JSON.stringify(payload, null, 2), 'utf8', (err) => {
          if (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to write data file' }));
            return;
          }
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true }));
        });
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload' }));
      }
    });
    return;
  }

  // 3. API: Sync to Obsidian
  if (req.method === 'POST' && pathname === '/api/sync-obsidian') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const { year, month, markdownContent } = JSON.parse(body);
        if (!year || !month || !markdownContent) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Missing parameters' }));
          return;
        }

        const obsidianDir = path.join(OBSIDIAN_VAULT, '記帳帳目');
        if (!fs.existsSync(obsidianDir)) {
          fs.mkdirSync(obsidianDir, { recursive: true });
        }

        const fileName = `${year}年${String(month).padStart(2, '0')}月_記帳統計.md`;
        const filePath = path.join(obsidianDir, fileName);

        fs.writeFile(filePath, markdownContent, 'utf8', (err) => {
          if (err) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: `Failed to write Obsidian file: ${err.message}` }));
            return;
          }
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true, path: filePath }));
        });
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload' }));
      }
    });
    return;
  }

  // 4. Static Files serving
  if (req.method === 'GET') {
    // Prevent directory traversal
    let safeSuffix = path.normalize(pathname).replace(/^(\.\.[\/\\])+/, '');
    if (safeSuffix === '/' || safeSuffix === '\\') {
      safeSuffix = 'index.html';
    }
    const filePath = path.join(PUBLIC_DIR, safeSuffix);

    fs.stat(filePath, (err, stats) => {
      if (err || !stats.isFile()) {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('404 Not Found');
        return;
      }

      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';

      res.writeHead(200, { 'Content-Type': contentType });
      const stream = fs.createReadStream(filePath);
      stream.pipe(res);
    });
    return;
  }

  // Fallback for unsupported methods
  res.writeHead(405, { 'Content-Type': 'text/plain' });
  res.end('Method Not Allowed');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`==================================================`);
  console.log(`  隨手記 (Money Flow) 本地伺服器已成功啟動！`);
  console.log(`==================================================`);
  console.log(`  電腦本機存取網址: http://localhost:${PORT}`);
  console.log(`--------------------------------------------------`);
  console.log(`  📱 iOS 手機存取方式 (需在同一 Wi-Fi 下):`);
  const ips = getLocalIPs();
  if (ips.length === 0) {
    console.log(`  [警告] 未偵測到有效的區域網路 IP，請確認電腦是否已連接 Wi-Fi。`);
  } else {
    ips.forEach(ip => {
      console.log(`  👉 http://${ip}:${PORT}`);
    });
  }
  console.log(`==================================================`);
  console.log(`  資料儲存路徑: ${DATA_FILE}`);
  console.log(`  Obsidian 庫路徑: ${OBSIDIAN_VAULT}`);
  console.log(`==================================================`);
});
