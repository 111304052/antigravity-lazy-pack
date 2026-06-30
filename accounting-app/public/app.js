// State Variables
let state = {
  transactions: [],
  accounts: []
};

let currentScreen = 'ledger';
let viewMode = 'calendar'; // 'calendar' or 'list'
let selectedDate = new Date();
let displayDate = new Date(); // Month currently viewed

// Editing State
let currentEditingTxId = null;
let transactionType = 'expense'; // 'expense', 'income', 'transfer'
let selectedCategory = '飲食';

// Calculator state
let calcValue = '0';
let calcFormula = '';
let isNewNumber = true;

// Constants
const CATEGORY_MAP = {
  '飲食': { icon: 'utensils', color: '#3b82f6' },       // Blue
  '日用品': { icon: 'shopping-bag', color: '#10b981' },  // Emerald
  '交通': { icon: 'car', color: '#f59e0b' },            // Amber
  '服飾': { icon: 'shirt', color: '#ec4899' },          // Pink
  '娛樂': { icon: 'gamepad-2', color: '#8b5cf6' },      // Violet
  '保養': { icon: 'sparkles', color: '#06b6d4' },       // Cyan
  '醫療': { icon: 'heart-pulse', color: '#ef4444' },     // Red
  '學習': { icon: 'graduation-cap', color: '#14b8a6' },  // Teal
  '運動': { icon: 'activity', color: '#84cc16' },        // Lime
  '水電': { icon: 'droplet', color: '#6366f1' },         // Indigo
  
  // Income categories
  '薪資': { icon: 'coins', color: '#10b981' },
  '投資': { icon: 'trending-up', color: '#3b82f6' },
  '獎金': { icon: 'award', color: '#eab308' },
  '其他': { icon: 'wallet-cards', color: '#71717a' },
  
  // Transfer category placeholder
  '轉帳': { icon: 'arrow-left-right', color: '#60a5fa' }
};

const ACCOUNT_NAMES = {
  'cash': '現金',
  'bank': '銀行',
  'card': '信用卡'
};

// Chart.js instance variable
let categoryChartInstance = null;
let activeChartType = 'expense';
let activeChartDimension = 'category';

// Receipt mock images store
let uploadedReceipts = [];

let isOfflineMode = false;
let hasUnsyncedChanges = localStorage.getItem('piggy_unsynced') === 'true';

// Update Sync status badge
function setSyncStatus(status) {
  const badge = document.getElementById('syncStatusBadge');
  const text = document.getElementById('syncStatusText');
  const icon = document.getElementById('syncStatusIcon');
  
  if (!badge || !text || !icon) return;
  
  badge.className = 'sync-status-badge ' + status;
  
  if (status === 'online') {
    text.innerText = '已連線';
    icon.setAttribute('data-lucide', 'cloud-check');
    isOfflineMode = false;
  } else if (status === 'offline') {
    text.innerText = hasUnsyncedChanges ? '離線中 (未同步)' : '離線中';
    icon.setAttribute('data-lucide', 'cloud-off');
    isOfflineMode = true;
  } else if (status === 'syncing') {
    text.innerText = '同步中...';
    icon.setAttribute('data-lucide', 'refresh-cw');
  }
  lucide.createIcons();
}

// Fetch data from server
async function loadData() {
  try {
    setSyncStatus('syncing');
    const response = await fetch('/api/data');
    if (!response.ok) throw new Error('Network response not ok');
    state = await response.json();
    
    // Auto calculate account balances based on transactions
    recalculateBalances();
    
    // If there were unsynced changes locally, we need to decide what to do.
    // In our state-based model, if the server loaded successfully and we had unsynced changes,
    // we can push our local unsynced changes back to the server.
    if (hasUnsyncedChanges) {
      const cached = localStorage.getItem('piggy_ledger');
      if (cached) {
        state = JSON.parse(cached);
        recalculateBalances();
        await pushChangesToServer();
      }
    } else {
      localStorage.setItem('piggy_ledger', JSON.stringify(state));
      setSyncStatus('online');
    }
    
    renderApp();
  } catch (error) {
    console.error('Error loading data:', error);
    setSyncStatus('offline');
    
    // Fallback to local storage
    const cached = localStorage.getItem('piggy_ledger');
    if (cached) {
      state = JSON.parse(cached);
      recalculateBalances();
      renderApp();
    }
  }
}

// Push local state to server
async function pushChangesToServer() {
  try {
    setSyncStatus('syncing');
    const response = await fetch('/api/save', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(state)
    });
    if (!response.ok) throw new Error('Save failed');
    hasUnsyncedChanges = false;
    localStorage.setItem('piggy_unsynced', 'false');
    setSyncStatus('online');
    return true;
  } catch (e) {
    console.error('Push to server failed:', e);
    setSyncStatus('offline');
    return false;
  }
}

// Save data locally and try to sync
async function saveData() {
  localStorage.setItem('piggy_ledger', JSON.stringify(state));
  hasUnsyncedChanges = true;
  localStorage.setItem('piggy_unsynced', 'true');
  
  const success = await pushChangesToServer();
  if (!success) {
    console.log('Saved to LocalStorage. Will sync when connection is restored.');
  }
}

// Background sync loop
setInterval(async () => {
  if (hasUnsyncedChanges && !isOfflineMode) {
    // Try to sync if we have changes and browser thinks we are online
    await pushChangesToServer();
  } else if (isOfflineMode) {
    // Ping server to see if back online
    try {
      const response = await fetch('/api/data', { method: 'HEAD' });
      if (response.ok) {
        loadData(); // Reload and sync
      }
    } catch (e) {
      // Still offline
    }
  }
}, 15000); // Check every 15 seconds

window.addEventListener('online', () => {
  if (hasUnsyncedChanges) {
    pushChangesToServer();
  } else {
    loadData();
  }
});

window.addEventListener('offline', () => {
  setSyncStatus('offline');
});


// Recalculate Account Balances dynamically
function recalculateBalances() {
  // Reset balances
  state.accounts = [
    { id: 'cash', name: '現金', balance: 0 },
    { id: 'bank', name: '銀行', balance: 0 },
    { id: 'card', name: '信用卡', balance: 0 }
  ];
  
  // Process each transaction
  state.transactions.forEach(tx => {
    const amount = parseFloat(tx.amount) || 0;
    if (tx.type === 'expense') {
      const acct = state.accounts.find(a => a.id === tx.accountId);
      if (acct) acct.balance -= amount;
    } else if (tx.type === 'income') {
      const acct = state.accounts.find(a => a.id === tx.accountId);
      if (acct) acct.balance += amount;
    } else if (tx.type === 'transfer') {
      const fromAcct = state.accounts.find(a => a.id === tx.fromAccountId);
      const toAcct = state.accounts.find(a => a.id === tx.toAccountId);
      const fee = parseFloat(tx.fee) || 0;
      
      if (fromAcct) fromAcct.balance -= (amount + fee);
      if (toAcct) toAcct.balance += amount;
    }
  });
}

// App Rendering controller
function renderApp() {
  updateHeader();
  if (currentScreen === 'ledger') {
    if (viewMode === 'calendar') {
      document.getElementById('calendarSection').style.display = 'block';
      renderCalendar();
    } else {
      document.getElementById('calendarSection').style.display = 'none';
      renderTransactionsList(getMonthTransactions(displayDate));
    }
    renderDailyTransactions();
  } else if (currentScreen === 'charts') {
    renderCharts();
  } else if (currentScreen === 'accounts') {
    renderAccounts();
  }
  lucide.createIcons();
}

function updateHeader() {
  const monthNames = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];
  const year = displayDate.getFullYear();
  const month = displayDate.getMonth();
  document.getElementById('currentMonthYear').innerText = `${year}年${monthNames[month]}`;
}

// Month Selector Logic
document.getElementById('monthSelectorBtn').addEventListener('click', () => {
  document.getElementById('pickerYearVal').innerText = displayDate.getFullYear();
  openModal('monthPickerModal');
});

function changePickerYear(offset) {
  const yearEl = document.getElementById('pickerYearVal');
  let year = parseInt(yearEl.innerText) + offset;
  yearEl.innerText = year;
}

function selectPickerMonth(monthIndex) {
  const year = parseInt(document.getElementById('pickerYearVal').innerText);
  displayDate = new Date(year, monthIndex, 1);
  selectedDate = new Date(year, monthIndex, 1); // Set selected date to first day of that month
  closeModal('monthPickerModal');
  renderApp();
}

// View toggle (Calendar vs List)
document.getElementById('btnToggleCalendar').addEventListener('click', (e) => {
  viewMode = 'calendar';
  document.getElementById('btnToggleCalendar').classList.add('active');
  document.getElementById('btnToggleList').classList.remove('active');
  renderApp();
});

document.getElementById('btnToggleList').addEventListener('click', (e) => {
  viewMode = 'list';
  document.getElementById('btnToggleList').classList.add('active');
  document.getElementById('btnToggleCalendar').classList.remove('active');
  renderApp();
});

// CALENDAR RENDERING
function renderCalendar() {
  const grid = document.getElementById('calendarGrid');
  grid.innerHTML = '';
  
  const year = displayDate.getFullYear();
  const month = displayDate.getMonth();
  
  // First day of month
  const firstDay = new Date(year, month, 1);
  const startDayOfWeek = firstDay.getDay(); // 0 is Sunday, 6 is Saturday
  
  // Total days in month
  const totalDays = new Date(year, month + 1, 0).getDate();
  
  // Total days in previous month
  const prevMonthTotalDays = new Date(year, month, 0).getDate();
  
  // Render empty cells from previous month
  for (let i = startDayOfWeek - 1; i >= 0; i--) {
    const day = prevMonthTotalDays - i;
    const cell = createDayCell(day, new Date(year, month - 1, day), true);
    grid.appendChild(cell);
  }
  
  // Render current month days
  const today = new Date();
  for (let day = 1; day <= totalDays; day++) {
    const date = new Date(year, month, day);
    const isToday = date.toDateString() === today.toDateString();
    const cell = createDayCell(day, date, false, isToday);
    grid.appendChild(cell);
  }
  
  // Render next month leading days to complete grid (multiples of 7)
  const currentTotalCells = startDayOfWeek + totalDays;
  const remainingCells = (7 - (currentTotalCells % 7)) % 7;
  for (let day = 1; day <= remainingCells; day++) {
    const cell = createDayCell(day, new Date(year, month + 1, day), true);
    grid.appendChild(cell);
  }
}

function createDayCell(day, date, isOtherMonth, isToday = false) {
  const cell = document.createElement('div');
  cell.classList.add('calendar-day-cell');
  
  if (isOtherMonth) cell.classList.add('other-month');
  
  if (isToday) {
    const badge = document.createElement('span');
    badge.classList.add('calendar-day-cell', 'today-badge');
    badge.innerText = day;
    cell.appendChild(badge);
  } else {
    cell.innerText = day;
  }
  
  // Match selected state
  if (date.toDateString() === selectedDate.toDateString()) {
    cell.classList.add('selected');
  }
  
  // Find transactions on this date to draw dots
  const dayTx = state.transactions.filter(tx => new Date(tx.date).toDateString() === date.toDateString());
  if (dayTx.length > 0) {
    const dotsContainer = document.createElement('div');
    dotsContainer.classList.add('dots-container');
    
    // Get unique types
    const types = [...new Set(dayTx.map(t => t.type))];
    types.forEach(type => {
      const dot = document.createElement('div');
      dot.classList.add('dot', type);
      dotsContainer.appendChild(dot);
    });
    cell.appendChild(dotsContainer);
  }
  
  // Click handler
  cell.addEventListener('click', () => {
    selectedDate = date;
    // Highlight active selected cell
    document.querySelectorAll('.calendar-day-cell').forEach(c => c.classList.remove('selected'));
    cell.classList.add('selected');
    renderDailyTransactions();
  });
  
  return cell;
}

// Get monthly transactions
function getMonthTransactions(date) {
  const y = date.getFullYear();
  const m = date.getMonth();
  return state.transactions.filter(tx => {
    const txDate = new Date(tx.date);
    return txDate.getFullYear() === y && txDate.getMonth() === m;
  });
}

// Render selected day's transactions in details list
function renderDailyTransactions() {
  const list = document.getElementById('dailyTransactionsList');
  const sumEl = document.getElementById('dailySummaryVal');
  const dateHeader = document.getElementById('selectedDateText');
  
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  dateHeader.innerText = selectedDate.toLocaleDateString('zh-TW', options);
  
  list.innerHTML = '';
  
  // Find transactions for selected date
  const dayTx = state.transactions.filter(tx => new Date(tx.date).toDateString() === selectedDate.toDateString());
  
  // Calculate day summary
  let dayExpense = 0;
  let dayIncome = 0;
  dayTx.forEach(tx => {
    const amt = parseFloat(tx.amount) || 0;
    if (tx.type === 'expense') dayExpense += amt;
    if (tx.type === 'income') dayIncome += amt;
  });
  
  sumEl.innerText = `支出: $${dayExpense.toLocaleString()} | 收入: $${dayIncome.toLocaleString()}`;
  
  if (dayTx.length === 0) {
    list.innerHTML = `
      <div class="empty-state">
        <i data-lucide="inbox"></i>
        <p>今天沒有記帳紀錄喔</p>
      </div>
    `;
    lucide.createIcons();
    return;
  }
  
  dayTx.forEach(tx => {
    const item = createTransactionDOMItem(tx);
    list.appendChild(item);
  });
  lucide.createIcons();
}

// Render complete month list when viewMode is 'list'
function renderTransactionsList(txs) {
  const list = document.getElementById('dailyTransactionsList');
  list.innerHTML = '';
  
  if (txs.length === 0) {
    list.innerHTML = `
      <div class="empty-state">
        <i data-lucide="inbox"></i>
        <p>此月份沒有記帳紀錄喔</p>
      </div>
    `;
    lucide.createIcons();
    return;
  }
  
  // Sort by date descending
  const sorted = [...txs].sort((a, b) => new Date(b.date) - new Date(a.date));
  
  // Group by date
  let currentDateGroup = '';
  let groupContainer = null;
  
  sorted.forEach(tx => {
    const dateStr = new Date(tx.date).toLocaleDateString('zh-TW', { month: 'long', day: 'numeric', weekday: 'short' });
    
    if (dateStr !== currentDateGroup) {
      currentDateGroup = dateStr;
      
      const groupHeader = document.createElement('div');
      groupHeader.classList.add('daily-header');
      groupHeader.style.padding = '12px 16px 4px 16px';
      groupHeader.style.borderBottom = 'none';
      groupHeader.style.backgroundColor = 'var(--bg-secondary)';
      groupHeader.innerHTML = `<span class="selected-date-text">${dateStr}</span>`;
      list.appendChild(groupHeader);
    }
    
    const item = createTransactionDOMItem(tx);
    list.appendChild(item);
  });
  
  lucide.createIcons();
}

function createTransactionDOMItem(tx) {
  const item = document.createElement('div');
  item.classList.add('tx-item');
  item.addEventListener('click', () => editTransaction(tx.id));
  
  const map = CATEGORY_MAP[tx.category] || { icon: 'help-circle', color: '#a1a1aa' };
  const symbol = tx.type === 'expense' ? '-' : (tx.type === 'income' ? '+' : '⇄');
  const typeClass = tx.type;
  
  let subDetails = '';
  if (tx.type === 'transfer') {
    subDetails = `${ACCOUNT_NAMES[tx.fromAccountId] || tx.fromAccountId} → ${ACCOUNT_NAMES[tx.toAccountId] || tx.toAccountId}`;
  } else {
    subDetails = ACCOUNT_NAMES[tx.accountId] || tx.accountId;
  }
  
  if (tx.remarks) {
    subDetails += ` | ${tx.remarks}`;
  }
  
  item.innerHTML = `
    <div class="tx-icon-wrapper" style="background-color: rgba(${hexToRgb(map.color)}, 0.15)">
      <i data-lucide="${map.icon}" style="color: ${map.color}"></i>
    </div>
    <div class="tx-details">
      <div class="tx-title-row">
        <span class="tx-category">${tx.category}</span>
        <span class="tx-amount ${typeClass}">${symbol}$${(parseFloat(tx.amount)||0).toLocaleString()}</span>
      </div>
      <div class="tx-sub-row">
        <span class="tx-remarks">${subDetails}</span>
        <span class="tx-account">${tx.member || '自己'}</span>
      </div>
    </div>
  `;
  return item;
}

// Convert Hex to RGB helper
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? 
    `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}` 
    : '255, 255, 255';
}

// Modal management
function openModal(modalId) {
  document.getElementById(modalId).classList.add('active');
}

function closeModal(modalId) {
  document.getElementById(modalId).classList.remove('active');
}

// Add transaction dialog
document.getElementById('btnOpenAddModal').addEventListener('click', () => {
  currentEditingTxId = null;
  // Initialize form fields
  document.getElementById('formDate').valueAsDate = selectedDate;
  calcValue = '0';
  calcFormula = '';
  document.getElementById('formAmountText').innerText = '0';
  document.getElementById('formAmount').value = '0';
  document.getElementById('formRemarks').value = '';
  document.getElementById('formTags').value = '';
  document.getElementById('calcFormulaDisplay').innerText = '';
  uploadedReceipts = [];
  renderReceiptThumbnails();
  
  // Default values
  setTransactionType('expense');
  
  document.getElementById('deleteBtnContainer').style.display = 'none';
  document.getElementById('calcKeyboard').classList.add('active');
  
  openModal('addTransactionModal');
  lucide.createIcons();
});

// Switch screen (Tab click)
function switchScreen(screenId) {
  currentScreen = screenId;
  document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  
  // Activate target
  if (screenId === 'ledger') {
    document.getElementById('screenLedger').classList.add('active');
    document.querySelectorAll('.nav-btn')[0].classList.add('active');
  } else if (screenId === 'charts') {
    document.getElementById('screenCharts').classList.add('active');
    document.querySelectorAll('.nav-btn')[1].classList.add('active');
  } else if (screenId === 'accounts') {
    document.getElementById('screenAccounts').classList.add('active');
    document.querySelectorAll('.nav-btn')[3].classList.add('active');
  } else if (screenId === 'settings') {
    document.getElementById('screenSettings').classList.add('active');
    document.querySelectorAll('.nav-btn')[4].classList.add('active');
  }
  
  renderApp();
}

// Setting transaction types in modal
function setTransactionType(type) {
  transactionType = type;
  document.getElementById('tabTypeExpense').classList.remove('active');
  document.getElementById('tabTypeIncome').classList.remove('active');
  document.getElementById('tabTypeTransfer').classList.remove('active');
  
  if (type === 'expense') {
    document.getElementById('tabTypeExpense').classList.add('active');
    document.getElementById('standardFields').style.display = 'block';
    document.getElementById('transferFields').style.display = 'none';
    selectedCategory = '飲食';
    renderCategoryGrid('expense');
  } else if (type === 'income') {
    document.getElementById('tabTypeIncome').classList.add('active');
    document.getElementById('standardFields').style.display = 'block';
    document.getElementById('transferFields').style.display = 'none';
    selectedCategory = '薪資';
    renderCategoryGrid('income');
  } else if (type === 'transfer') {
    document.getElementById('tabTypeTransfer').classList.add('active');
    document.getElementById('standardFields').style.display = 'none';
    document.getElementById('transferFields').style.display = 'block';
    selectedCategory = '轉帳';
  }
}

function renderCategoryGrid(type) {
  const container = document.getElementById('categoryGridList');
  container.innerHTML = '';
  
  let categories = [];
  if (type === 'expense') {
    categories = ['飲食', '日用品', '交通', '服飾', '娛樂', '保養', '醫療', '學習', '運動', '水電'];
  } else {
    categories = ['薪資', '投資', '獎金', '其他'];
  }
  
  categories.forEach(cat => {
    const map = CATEGORY_MAP[cat] || { icon: 'help-circle', color: '#a1a1aa' };
    const cell = document.createElement('div');
    cell.classList.add('category-cell');
    if (cat === selectedCategory) cell.classList.add('active');
    
    cell.innerHTML = `
      <div class="category-icon">
        <i data-lucide="${map.icon}"></i>
      </div>
      <span class="category-name">${cat}</span>
    `;
    
    cell.addEventListener('click', () => {
      selectedCategory = cat;
      document.querySelectorAll('.category-cell').forEach(c => c.classList.remove('active'));
      cell.classList.add('active');
    });
    
    container.appendChild(cell);
  });
  lucide.createIcons();
}

// Dynamic Numpad Calculator logic
const calculatorDisplayBox = document.getElementById('amountDisplayBox');
const calculatorKeyboard = document.getElementById('calcKeyboard');

calculatorDisplayBox.addEventListener('click', () => {
  calculatorKeyboard.classList.toggle('active');
});

const calcButtons = document.querySelectorAll('.calc-btn');
calcButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const val = btn.getAttribute('data-val');
    const action = btn.getAttribute('data-action');
    
    if (val) {
      handleNumInput(val);
    } else if (action) {
      handleActionInput(action);
    }
  });
});

function handleNumInput(num) {
  if (isNewNumber) {
    calcValue = num === '.' ? '0.' : num;
    isNewNumber = false;
  } else {
    if (num === '.' && calcValue.includes('.')) return;
    calcValue += num;
  }
  updateCalcDisplay();
}

function handleActionInput(action) {
  if (action === '⌫') {
    if (calcValue.length > 1) {
      calcValue = calcValue.slice(0, -1);
    } else {
      calcValue = '0';
      isNewNumber = true;
    }
    updateCalcDisplay();
  } else if (action === 'C') {
    calcValue = '0';
    calcFormula = '';
    isNewNumber = true;
    updateCalcDisplay();
  } else if (['+', '-', '×', '÷'].includes(action)) {
    // If there is already a formula, evaluate it first or chain it
    if (calcFormula !== '') {
      evaluateFormula(false);
    }
    calcFormula = `${calcValue} ${action} `;
    isNewNumber = true;
    updateCalcDisplay();
  } else if (action === '=') {
    evaluateFormula(true);
  } else if (action === '00' || action === '000') {
    if (isNewNumber || calcValue === '0') return;
    calcValue += action;
    updateCalcDisplay();
  }
}

function evaluateFormula(clearFormula = true) {
  if (!calcFormula) return;
  
  // Format math expression
  let expr = calcFormula + calcValue;
  expr = expr.replace(/×/g, '*').replace(/÷/g, '/');
  
  try {
    // Clean string using regex to protect security
    if (/^[0-9+\-*/.\s]+$/.test(expr)) {
      // Evaluate expression
      const result = new Function(`return (${expr})`)();
      if (isFinite(result)) {
        // Round to 2 decimal places to avoid floating point issues
        calcValue = String(Math.round(result * 100) / 100);
      } else {
        calcValue = '0';
      }
    } else {
      calcValue = '0';
    }
  } catch (e) {
    calcValue = '0';
  }
  
  calcFormula = clearFormula ? '' : calcValue;
  isNewNumber = true;
  updateCalcDisplay();
}

function updateCalcDisplay() {
  document.getElementById('formAmountText').innerText = parseFloat(calcValue).toLocaleString('zh-TW', { maximumFractionDigits: 2 });
  document.getElementById('formAmount').value = calcValue;
  document.getElementById('calcFormulaDisplay').innerText = calcFormula;
}

// Edit existing transaction
function editTransaction(id) {
  const tx = state.transactions.find(t => t.id === id);
  if (!tx) return;
  
  currentEditingTxId = id;
  
  // Fill details
  document.getElementById('formDate').value = tx.date;
  calcValue = String(tx.amount);
  calcFormula = '';
  updateCalcDisplay();
  
  setTransactionType(tx.type);
  
  if (tx.type === 'transfer') {
    document.getElementById('formFromAccount').value = tx.fromAccountId;
    document.getElementById('formToAccount').value = tx.toAccountId;
    document.getElementById('formTransferFee').value = tx.fee || 0;
  } else {
    selectedCategory = tx.category;
    renderCategoryGrid(tx.type);
    document.getElementById('formAccount').value = tx.accountId;
    document.getElementById('formMember').value = tx.member || '自己';
  }
  
  document.getElementById('formRemarks').value = tx.remarks || '';
  document.getElementById('formTags').value = (tx.tags || []).join(' ');
  
  uploadedReceipts = tx.receipts || [];
  renderReceiptThumbnails();
  
  document.getElementById('deleteBtnContainer').style.display = 'block';
  document.getElementById('calcKeyboard').classList.remove('active'); // Close numpad on load so form is visible
  
  openModal('addTransactionModal');
  lucide.createIcons();
}

// Save Transaction handler
document.getElementById('btnSaveTransaction').addEventListener('click', async () => {
  // If keyboard formula is active, resolve it first
  if (calcFormula !== '') {
    evaluateFormula(true);
  }
  
  const amount = parseFloat(document.getElementById('formAmount').value) || 0;
  if (amount <= 0) {
    alert('請輸入大於 0 的金額');
    return;
  }
  
  const date = document.getElementById('formDate').value;
  const remarks = document.getElementById('formRemarks').value;
  const tagsString = document.getElementById('formTags').value;
  const tags = tagsString.trim() ? tagsString.trim().split(/\s+/) : [];
  
  let newTx = {
    id: currentEditingTxId || generateId(),
    date,
    amount,
    type: transactionType,
    category: selectedCategory,
    remarks,
    tags,
    receipts: uploadedReceipts
  };
  
  if (transactionType === 'transfer') {
    const fromId = document.getElementById('formFromAccount').value;
    const toId = document.getElementById('formToAccount').value;
    const fee = parseFloat(document.getElementById('formTransferFee').value) || 0;
    
    if (fromId === toId) {
      alert('來源帳戶與目標帳戶不可相同');
      return;
    }
    
    newTx.fromAccountId = fromId;
    newTx.toAccountId = toId;
    newTx.fee = fee;
    newTx.category = '轉帳';
  } else {
    newTx.accountId = document.getElementById('formAccount').value;
    newTx.member = document.getElementById('formMember').value;
  }
  
  if (currentEditingTxId) {
    // Modify existing
    const idx = state.transactions.findIndex(t => t.id === currentEditingTxId);
    state.transactions[idx] = newTx;
  } else {
    // Add new
    state.transactions.push(newTx);
  }
  
  recalculateBalances();
  await saveData();
  closeModal('addTransactionModal');
  
  // Set display date to saved transaction month to easily view it
  const savedDate = new Date(date);
  displayDate = new Date(savedDate.getFullYear(), savedDate.getMonth(), 1);
  selectedDate = savedDate;
  
  renderApp();
});

// Delete Transaction handler
document.getElementById('btnDeleteTransaction').addEventListener('click', async () => {
  if (!currentEditingTxId) return;
  
  if (confirm('確定要刪除此筆記帳明細嗎？')) {
    state.transactions = state.transactions.filter(t => t.id !== currentEditingTxId);
    recalculateBalances();
    await saveData();
    closeModal('addTransactionModal');
    renderApp();
  }
});

// Helper: ID generator
function generateId() {
  return '_' + Math.random().toString(36).substr(2, 9);
}

// SCREEN 2: CHARTS RENDERING
const ACCOUNT_COLORS = {
  'cash': '#3b82f6', // Blue
  'bank': '#10b981', // Green
  'card': '#ec4899'  // Pink
};

const MEMBER_COLORS = {
  '自己': '#f97316', // Orange
  '父母': '#06b6d4', // Cyan
  '爺爺': '#8b5cf6', // Violet
  '家族': '#eab308', // Yellow
  '朋友': '#a1a1aa'  // Gray
};

function getDimensionColor(key, dim) {
  if (dim === 'category') {
    return (CATEGORY_MAP[key] || { color: '#a1a1aa' }).color;
  } else if (dim === 'account') {
    return ACCOUNT_COLORS[key] || '#71717a';
  } else if (dim === 'member') {
    if (MEMBER_COLORS[key]) return MEMBER_COLORS[key];
    // Generate stable color from string hash
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = key.charCodeAt(i) + ((hash << 5) - hash);
    }
    const color = (hash & 0x00FFFFFF).toString(16).toUpperCase();
    return '#' + '00000'.substring(0, 6 - color.length) + color;
  }
  return '#a1a1aa';
}

function getDimensionLabel(key, dim) {
  if (dim === 'account') {
    return ACCOUNT_NAMES[key] || key;
  }
  return key; // Category and Member are already plain text labels
}

function setChartType(type) {
  activeChartType = type;
  document.getElementById('btnChartTypeExpense').classList.toggle('active', type === 'expense');
  document.getElementById('btnChartTypeIncome').classList.toggle('active', type === 'income');
  renderCharts();
}

function setChartDimension(dim) {
  activeChartDimension = dim;
  document.getElementById('btnChartDimCategory').classList.toggle('active', dim === 'category');
  document.getElementById('btnChartDimAccount').classList.toggle('active', dim === 'account');
  document.getElementById('btnChartDimMember').classList.toggle('active', dim === 'member');
  renderCharts();
}

function renderCharts() {
  const txs = getMonthTransactions(displayDate);
  const filtered = txs.filter(t => t.type === activeChartType);
  
  // Aggregate amounts by the selected dimension
  const groups = {};
  let totalSum = 0;
  
  filtered.forEach(t => {
    const amt = parseFloat(t.amount) || 0;
    let groupKey = '';
    
    if (activeChartDimension === 'category') {
      groupKey = t.category;
    } else if (activeChartDimension === 'account') {
      groupKey = t.accountId || 'cash';
    } else if (activeChartDimension === 'member') {
      groupKey = t.member || '自己';
    }
    
    groups[groupKey] = (groups[groupKey] || 0) + amt;
    totalSum += amt;
  });
  
  document.getElementById('chartTotalSum').innerText = `$${totalSum.toLocaleString()}`;
  
  // Calculate average daily
  const year = displayDate.getFullYear();
  const month = displayDate.getMonth();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const avg = Math.round(totalSum / daysInMonth);
  document.getElementById('chartDailyAvg').innerText = `$${avg.toLocaleString()}`;
  
  // Sort data by amount descending
  const dataArray = Object.keys(groups).map(key => {
    return {
      key: key,
      name: getDimensionLabel(key, activeChartDimension),
      amount: groups[key],
      percentage: totalSum > 0 ? (groups[key] / totalSum * 100) : 0,
      color: getDimensionColor(key, activeChartDimension)
    };
  }).sort((a, b) => b.amount - a.amount);
  
  // Render details list
  const listContainer = document.getElementById('chartCategoryList');
  listContainer.innerHTML = '';
  
  const typeLabel = activeChartType === 'expense' ? '支出' : '收入';
  const dimLabel = activeChartDimension === 'category' ? '類別' : (activeChartDimension === 'account' ? '帳戶' : '成員');
  
  if (dataArray.length === 0) {
    listContainer.innerHTML = `<div class="empty-state"><p>本月無任何 ${typeLabel} 記錄</p></div>`;
  } else {
    dataArray.forEach((item, idx) => {
      const row = document.createElement('div');
      row.classList.add('chart-row');
      
      row.innerHTML = `
        <span class="chart-row-index">${idx + 1}</span>
        <div class="chart-row-color" style="background-color: ${item.color}"></div>
        <span class="chart-row-name">${item.name}</span>
        <div class="chart-row-vals">
          <span class="chart-row-amount">$${item.amount.toLocaleString()}</span>
          <span class="chart-row-percent">${item.percentage.toFixed(1)}%</span>
        </div>
      `;
      listContainer.appendChild(row);
    });
  }
  
  // Render ChartJS Donut
  const ctx = document.getElementById('categoryChart').getContext('2d');
  
  if (categoryChartInstance) {
    categoryChartInstance.destroy();
  }
  
  if (dataArray.length === 0) {
    // Draw an empty gray circle if no data
    categoryChartInstance = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['無資料'],
        datasets: [{
          data: [1],
          backgroundColor: ['#27272a'],
          borderWidth: 0
        }]
      },
      options: {
        cutout: '75%',
        plugins: { legend: { display: false }, tooltip: { enabled: false } },
        responsive: true,
        maintainAspectRatio: false
      }
    });
    return;
  }
  
  const labels = dataArray.map(d => d.name);
  const data = dataArray.map(d => d.amount);
  const colors = dataArray.map(d => d.color);
  
  categoryChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        backgroundColor: colors,
        borderWidth: 1,
        borderColor: '#121214'
      }]
    },
    options: {
      cutout: '70%',
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(context) {
              const val = context.raw || 0;
              const percent = (val / totalSum * 100).toFixed(1);
              return ` ${context.label}: $${val.toLocaleString()} (${percent}%)`;
            }
          }
        }
      },
      responsive: true,
      maintainAspectRatio: false
    }
  });
}

// SCREEN 3: ACCOUNTS RENDERING
function renderAccounts() {
  const container = document.getElementById('accountsListContainer');
  const netWorthVal = document.getElementById('totalNetWorth');
  container.innerHTML = '';
  
  let netWorth = 0;
  
  state.accounts.forEach(acct => {
    netWorth += acct.balance;
    
    const card = document.createElement('div');
    card.classList.add('account-card');
    
    let iconName = 'wallet';
    if (acct.id === 'bank') iconName = 'landmark';
    if (acct.id === 'card') iconName = 'credit-card';
    
    const balClass = acct.balance >= 0 ? '' : 'expense';
    const formattedBalance = acct.balance >= 0 ? 
      `$${acct.balance.toLocaleString()}` : 
      `-$${Math.abs(acct.balance).toLocaleString()}`;
    
    card.innerHTML = `
      <div class="account-card-left">
        <div class="account-card-icon">
          <i data-lucide="${iconName}"></i>
        </div>
        <span class="account-card-name">${acct.name}</span>
      </div>
      <span class="account-card-balance ${balClass}">${formattedBalance}</span>
    `;
    
    container.appendChild(card);
  });
  
  const formattedNetWorth = netWorth >= 0 ? 
    `$${netWorth.toLocaleString()}` : 
    `-$${Math.abs(netWorth).toLocaleString()}`;
    
  netWorthVal.innerText = formattedNetWorth;
  if (netWorth < 0) {
    netWorthVal.classList.add('expense');
  } else {
    netWorthVal.classList.remove('expense');
  }
}

// SCREEN 4: SETTINGS ACTIONS
// 1. Sync to Obsidian
document.getElementById('btnSyncObsidian').addEventListener('click', async () => {
  const year = displayDate.getFullYear();
  const month = displayDate.getMonth() + 1;
  
  // Fetch monthly transactions
  const txs = getMonthTransactions(displayDate);
  if (txs.length === 0) {
    alert(`此月份 (${year}年${month}月) 無任何記帳資料，無需同步`);
    return;
  }
  
  // Format monthly summary to markdown
  let expenseSum = 0;
  let incomeSum = 0;
  const categoriesSum = {};
  
  txs.forEach(t => {
    const amt = parseFloat(t.amount) || 0;
    if (t.type === 'expense') {
      expenseSum += amt;
      categoriesSum[t.category] = (categoriesSum[t.category] || 0) + amt;
    } else if (t.type === 'income') {
      incomeSum += amt;
    }
  });
  
  const netValue = incomeSum - expenseSum;
  
  let md = `# 📊 ${year} 年 ${String(month).padStart(2, '0')} 月記帳統計報告\n\n`;
  md += `> [!NOTE]\n`;
  md += `> 資料更新時間：${new Date().toLocaleString('zh-TW')}\n`;
  md += `> 系統本機資料檔案：\`accounting-app/data/ledger.json\`\n\n`;
  
  md += `## 💰 財務總覽\n\n`;
  md += `| 項目 | 金額 |\n`;
  md += `| :--- | :--- |\n`;
  md += `| 📈 **總收入** | \`+$${incomeSum.toLocaleString()}\` |\n`;
  md += `| 📉 **總支出** | \`-$${expenseSum.toLocaleString()}\` |\n`;
  md += `| ⚖️ **結餘 (收支差)** | \`${netValue >= 0 ? '+' : ''}$${netValue.toLocaleString()}\` |\n\n`;
  
  md += `## 🍩 支出類別佔比\n\n`;
  md += `| 類別 | 支出金額 | 比例 |\n`;
  md += `| :--- | :--- | :--- |\n`;
  
  const sortedCats = Object.keys(categoriesSum).map(c => {
    return { name: c, amount: categoriesSum[c], percent: expenseSum > 0 ? (categoriesSum[c] / expenseSum * 100) : 0 };
  }).sort((a, b) => b.amount - a.amount);
  
  sortedCats.forEach(c => {
    md += `| ${c.name} | $${c.amount.toLocaleString()} | ${c.percent.toFixed(1)}% |\n`;
  });
  
  md += `\n## 📝 明細清單\n\n`;
  md += `| 日期 | 類型 | 類別 | 金額 | 帳戶 | 成員 | 備註 |\n`;
  md += `| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n`;
  
  // Sort transactions by date ascending
  const sortedTxs = [...txs].sort((a, b) => new Date(a.date) - new Date(b.date));
  sortedTxs.forEach(t => {
    const symbol = t.type === 'expense' ? '-' : (t.type === 'income' ? '+' : '⇄');
    let acctDetail = '';
    if (t.type === 'transfer') {
      acctDetail = `${ACCOUNT_NAMES[t.fromAccountId] || t.fromAccountId}→${ACCOUNT_NAMES[t.toAccountId] || t.toAccountId}`;
    } else {
      acctDetail = ACCOUNT_NAMES[t.accountId] || t.accountId;
    }
    const typeLabel = t.type === 'expense' ? '支出' : (t.type === 'income' ? '收入' : '轉帳');
    const tagsString = (t.tags || []).length > 0 ? ` (標籤: ${t.tags.join(', ')})` : '';
    
    md += `| ${t.date} | ${typeLabel} | ${t.category} | ${symbol}$${t.amount} | ${acctDetail} | ${t.member || '自己'} | ${t.remarks || ''}${tagsString} |\n`;
  });
  
  md += `\n---\n*本統計報表由 **Antigravity 隨手記** 自動同步生成。*`;
  
  try {
    const response = await fetch('/api/sync-obsidian', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        year,
        month,
        markdownContent: md
      })
    });
    
    const result = await response.json();
    if (result.success) {
      alert(`已成功同步匯出！\n\n檔案位置：\n${result.path}`);
    } else {
      throw new Error(result.error);
    }
  } catch (error) {
    alert(`同步失敗：${error.message}`);
  }
});

// 2. Export Backup (JSON)
document.getElementById('btnBackupExport').addEventListener('click', () => {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  const stamp = new Date().toISOString().slice(0, 10);
  downloadAnchor.setAttribute("download", `隨手記_備份_${stamp}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
});

// 3. Import Backup (JSON)
document.getElementById('btnBackupImport').addEventListener('change', (e) => {
  const fileReader = new FileReader();
  if (e.target.files.length === 0) return;
  
  fileReader.onload = async (event) => {
    try {
      const parsed = JSON.parse(event.target.result);
      if (parsed.transactions && parsed.accounts) {
        if (confirm('匯入備份將會覆蓋您現有的記帳明細，確定要匯入嗎？')) {
          state = parsed;
          recalculateBalances();
          await saveData();
          renderApp();
          alert('備份匯入成功！');
        }
      } else {
        alert('無效的備份檔案格式');
      }
    } catch (err) {
      alert('解析檔案失敗，請確保上傳的是正確的備份 JSON 檔案');
    }
  };
  fileReader.readAsText(e.target.files[0]);
});

// 4. Clear all data
document.getElementById('btnClearData').addEventListener('click', async () => {
  if (confirm('⚠️ 警告！這將會清除您所有的記帳資料與歷史明細，且無法復原。確定要繼續嗎？')) {
    state.transactions = [];
    recalculateBalances();
    await saveData();
    renderApp();
    alert('已清除所有記帳紀錄');
  }
});

// MOCK CAMERA UPLOAD FOR RECEIPTS
document.getElementById('btnUploadReceipt').addEventListener('click', () => {
  document.getElementById('receiptFileInput').click();
});

document.getElementById('receiptFileInput').addEventListener('change', (e) => {
  const files = e.target.files;
  if (!files || files.length === 0) return;
  
  const remainingSlots = 3 - uploadedReceipts.length;
  const filesToProcess = Math.min(files.length, remainingSlots);
  
  if (filesToProcess <= 0) {
    alert('最多只能上傳 3 張收據照片喔');
    return;
  }
  
  for (let i = 0; i < filesToProcess; i++) {
    const file = files[i];
    const reader = new FileReader();
    
    reader.onload = function(event) {
      uploadedReceipts.push(event.target.result); // Base64 data url
      renderReceiptThumbnails();
    };
    reader.readAsDataURL(file);
  }
});

function renderReceiptThumbnails() {
  const container = document.getElementById('receiptThumbnails');
  container.innerHTML = '';
  
  uploadedReceipts.forEach((src, idx) => {
    const thumb = document.createElement('div');
    thumb.classList.add('receipt-thumb');
    
    thumb.innerHTML = `
      <img src="${src}">
      <div class="receipt-thumb-del" onclick="deleteReceipt(${idx})">
        <i data-lucide="x"></i>
      </div>
    `;
    container.appendChild(thumb);
  });
  
  // Show/Hide Add button
  const addBtn = document.getElementById('btnUploadReceipt');
  if (uploadedReceipts.length >= 3) {
    addBtn.style.display = 'none';
  } else {
    addBtn.style.display = 'flex';
  }
  
  lucide.createIcons();
}

// Global scope helper for deleting receipt thumbnail
window.deleteReceipt = function(idx) {
  uploadedReceipts.splice(idx, 1);
  renderReceiptThumbnails();
};

// Initialize App
loadData();
window.switchScreen = switchScreen;
window.changePickerYear = changePickerYear;
window.selectPickerMonth = selectPickerMonth;
window.changeChartTab = changeChartTab;
window.closeModal = closeModal;
window.setTransactionType = setTransactionType;
