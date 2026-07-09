/**
 * SkillPulse Learning Assistant Engine
 * Manages local diagnostics and Gemini API calls
 */

class SkillAssistant {
  constructor() {
    this.apiKey = localStorage.getItem('gemini_api_key') || null;
    this.systemContext = `
你是一位專業的資料科學與資料工程導師 (Data Science & Data Engineering Mentor)。
使用者的背景特點如下：
1. **統計學背景**：主修統計學，具備紮實的機率論與數理統計理論基礎。精通基本數據分析程式語言 (Python、R)。
2. **資訊技能學習中**：目前正在學習網頁爬取與設計、SQL 資料庫程式編寫、Git 版本控制等。
3. **經濟與財金基礎**：修習過總體經濟學、個體經濟學與投資學，具備基礎的財經觀念。
4. **未來目標**：希望能往資料工程 (Data Engineering) 領域持續深耕。

請以繁體中文 (zh-TW) 提供回覆，口吻應專業、具啟發性且親切，給予具體的學習步驟、學習資源或專案實作建議。
`;
  }

  setApiKey(key) {
    this.apiKey = key;
    if (key) {
      localStorage.setItem('gemini_api_key', key);
    } else {
      localStorage.removeItem('gemini_api_key');
    }
  }

  hasApiKey() {
    return !!this.apiKey;
  }

  /**
   * Main answer entrypoint.
   * If API Key is present, calls Gemini. Otherwise uses Local Diagnostic Engine.
   */
  async getResponse(userMessage, currentSkills, onChunk = null) {
    if (this.apiKey) {
      try {
        return await this.callGeminiAPI(userMessage, currentSkills, onChunk);
      } catch (err) {
        console.error("Gemini API Error, falling back to local engine:", err);
        return `⚠️ **Gemini API 呼叫失敗：** ${err.message}\n\n以下由**本機診斷引擎**為您回答：\n\n` + this.getLocalResponse(userMessage, currentSkills);
      }
    } else {
      // Simulate typing latency
      await new Promise(resolve => setTimeout(resolve, 800));
      return this.getLocalResponse(userMessage, currentSkills);
    }
  }

  /**
   * Call Gemini API via Fetch
   */
  async callGeminiAPI(userMessage, currentSkills, onChunk = null) {
    const cleanSkills = currentSkills.map(s => ({
      name: s.label,
      category: this.getCategoryName(s.category),
      status: this.getStatusName(s.status),
      description: s.description || ""
    }));

    const promptText = `
使用者目前的技能樹狀態 (JSON)：
${JSON.stringify(cleanSkills, null, 2)}

使用者提問：
"${userMessage}"

請結合使用者的統計背景、現有經濟學基礎，以及正在學習的網頁設計/SQL/Git進度，針對使用者的提問給予深度的個人化學習方向、專案設計或學習資源建議。特別注意他未來想往「資料工程」發展。
`;

    // Using gemini-1.5-flash for speed and reliability
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${this.apiKey}`;
    
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        contents: [
          {
            role: 'user',
            parts: [{ text: this.systemContext + "\n\n" + promptText }]
          }
        ],
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 2048
        }
      })
    });

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      throw new Error(errData?.error?.message || `HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    const resultText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    
    if (!resultText) {
      throw new Error("無效的 API 回應格式");
    }

    return this.markdownToHtml(resultText);
  }

  /**
   * Local Rule-based Response Engine
   */
  getLocalResponse(userMessage, currentSkills) {
    const msg = userMessage.toLowerCase();
    
    // Categorize current skills for context
    const mastered = currentSkills.filter(s => s.status === 'mastered');
    const learning = currentSkills.filter(s => s.status === 'learning');
    const planned = currentSkills.filter(s => s.status === 'planned');

    // Case 1: Combine Stats & Coding
    if (msg.includes('統計') && (msg.includes('程式') || msg.includes('應用') || msg.includes('python') || msg.includes('r'))) {
      return `
<h3>💡 如何結合統計理論與程式語言？</h3>
<p>你擁有<strong>機率論與數理統計</strong>的深厚理論基礎，這是許多程式設計師最缺乏的「內功」。結合 Python 與 R，你可以往以下方向發展：</p>
<ul>
  <li><strong>統計模擬與蒙地卡羅方法 (Monte Carlo Simulation)</strong>：利用 Python (numpy) 撰寫隨機抽樣演算法，視覺化大數法則與中央極限定理的收斂過程。這在計量經濟學和風險管理中極為實用。</li>
  <li><strong>假設檢定與推論自動化</strong>：你已掌握 A/B Testing 的統計學基礎（Z檢定、t檢定、卡方檢定）。利用 Python (scipy.stats) 或 R 建立自動化檢定腳本，分析網頁爬蟲收集下來的數據。</li>
  <li><strong>機器學習理論理解</strong>：統計學中的「迴歸分析」與「最大概似估計 (MLE)」是機器學習（例如邏輯迴歸、線性迴歸、貝氏分類器）的核心。你可以嘗試用 Python 從零手寫這些演算法，而非直接調用套件，這能極大發揮你的統計優勢。</li>
</ul>
<p><strong>🛠️ 建議小專案：A/B Testing 網頁成效分析</strong><br>
利用你的<strong>網頁設計</strong>技能做出一個有兩個版本的簡易登入頁面，收集使用者點擊數據，接著用 <strong>Python 進行假設檢定</strong>，評估兩組轉化率是否有顯著差異。</p>
`;
    }

    // Case 2: Data Engineering Transition Path
    if (msg.includes('資料工程') || msg.includes('de') || msg.includes('database') || msg.includes('sql') || msg.includes('管道') || msg.includes('pipeline')) {
      return `
<h3>📊 資料工程 (Data Engineering) 學習路徑建議</h3>
<p>資料工程的核心是「建置與維護穩定、高效的資料流管道(ETL/ELT)」。從你的背景出發，建議的升級路徑如下：</p>
<ol>
  <li><strong>精通資料庫與 SQL (你正在學習中)</strong>：
    <ul>
      <li>掌握多表關聯 (JOIN)、子查詢、視窗函數 (Window Functions) 以及資料庫索引 (Index) 優化。這是 DE 的核心基石。</li>
    </ul>
  </li>
  <li><strong>提升 Python 腳本編寫能力</strong>：
    <ul>
      <li>學習如何使用 Python 進行資料轉換（如 <code>pandas</code>, <code>polars</code>）。</li>
      <li>學習如何使用 Python 連接資料庫（如 <code>SQLAlchemy</code>, <code>psycopg2</code>）。</li>
    </ul>
  </li>
  <li><strong>學習 ETL/ELT 工具與排程</strong>：
    <ul>
      <li><strong>資料爬取 (你正在學習)</strong>：這就是 ETL 中的 "Extract" (萃取)。學習如何處理 API、JSON，並使用 <strong>Git</strong> 進行代碼版本控制。</li>
      <li><strong>工作流排程</strong>：學習 <code>Apache Airflow</code> 或 <code>Prefect</code>，自動化運行你的爬蟲與資料導入腳本。</li>
    </ul>
  </li>
  <li><strong>大數據與雲端平台 (你的計畫中技能)</strong>：
    <ul>
      <li>學習分佈式計算框架 <code>Apache Spark</code> (配合 PySpark)，因為統計學的大數據量分析往往需要分佈式運算。</li>
      <li>熟悉一門雲端服務（AWS, GCP 或 Azure）的資料湖與資料倉庫解決方案。</li>
    </ul>
  </li>
</ol>
<p><strong>🎯 當前重點</strong>：將 SQL 與 Python 結合。試著寫一個 Python 爬蟲，將爬取到的財金或社群數據自動清洗後，寫入 SQLite 或 PostgreSQL 資料庫中。</p>
`;
    }

    // Case 3: Econ & Finance combined with Scraping & SQL
    if (msg.includes('經濟') || msg.includes('財金') || msg.includes('投資') || msg.includes('金融') || msg.includes('總體') || msg.includes('個體')) {
      return `
<h3>💰 經濟財金觀念 x 數據爬蟲 x 資料庫專案規劃</h3>
<p>你具備個體經濟、總體經濟及投資學的素養，這讓你擁有極佳的「商業敏銳度 (Business Acumen)」。結合技術，你可以做出令人驚豔的量化專案：</p>
<ul>
  <li><strong>總體經濟指標監控儀表板 (Dashboard)</strong>：
    <ul>
      <li><strong>資料爬取</strong>：使用 Python 寫爬蟲，從政府公開 API、財經網站爬取通膨率、利率、GDP 成長率等數據。</li>
      <li><strong>資料庫儲存</strong>：將歷史數據結構化儲存在 <strong>SQL</strong> 中，設計合適的 schema。</li>
      <li><strong>分析與預測</strong>：利用 <strong>R</strong> 或 <strong>Python (statsmodels)</strong> 進行時間序列分析（如 ARIMA 機器學習預測），驗證總體經濟理論對股市的預測力。</li>
    </ul>
  </li>
  <li><strong>投資學：多因子選股與回測系統 (Backtesting)</strong>：
    <ul>
      <li>在 SQL 資料庫中建立上市櫃公司的財務報表數據庫（本益比、ROE、營收成長率）。</li>
      <li>使用 Python 撰寫回測腳本，根據你的投資學理論設定篩選因子，計算歷史投資報酬率與 Sharp Ratio。</li>
    </ul>
  </li>
</ul>
<p><strong>🛠️ 建議小專案：外匯與通膨關聯度分析</strong><br>
爬取各國通膨數據與匯率走勢，將其存入 SQL。利用 R 進行迴歸分析，探討購買力平價理論 (PPP) 在近五年的有效性，並使用 Git 記錄你的分析程式碼與報告。</p>
`;
    }

    // Case 4: Diagnostic / Learning Progress Analysis
    if (msg.includes('診斷') || msg.includes('進度') || msg.includes('盲點') || msg.includes('現況')) {
      const total = currentSkills.length;
      const statsCount = currentSkills.filter(s => s.category === 'statistics').length;
      const progCount = currentSkills.filter(s => s.category === 'programming').length;
      const econCount = currentSkills.filter(s => s.category === 'economics').length;
      const deCount = currentSkills.filter(s => s.category === 'data_engineering').length;

      return `
<h3>🔍 SkillPulse 個人學習現況診斷</h3>
<p>根據目前技能樹上的數據（共計 ${total} 個節點）：</p>
<ul>
  <li><strong>領域分布</strong>：統計與數學 (${statsCount} 節點) | 程式與資工 (${progCount} 節點) | 經濟財金 (${econCount} 節點) | 資料工程 (${deCount} 節點)</li>
  <li><strong>狀態統計</strong>：已掌握 ${mastered.length} 項 | 學習中 ${learning.length} 項 | 已規劃 ${planned.length} 項</li>
</ul>

<h4>💪 你的競爭優勢</h4>
<p>你擁有極佳的<strong>跨領域潛力</strong>。你的「統計理論」加上「經濟直覺」，在金融科技或數據分析領域是黃金組合。而你目前正在主動補強「程式（Python）」與「資料庫（SQL）」，這正是將理論轉化為實際商業產出的橋樑。</p>

<h4>⚠️ 學習盲點與建議補強</h4>
<ol>
  <li><strong>Git 與版本控制的落實</strong>：當你在做爬蟲與網頁設計時，請務必開始使用 Git。這不僅能記錄代碼，也是資料工程團隊協作的硬性要求。</li>
  <li><strong>SQL 理論與實踐的結合</strong>：不要只停留在寫 Select 查詢。嘗試去理解資料庫的結構設計 (Schema Design)，例如一對多、多對多關係，這對未來的 DE 發展至關重要。</li>
  <li><strong>程式語言的專注度</strong>：你同時掌握 Python 與 R。在往資料工程發展時，<strong>建議將 Python 作為主力語言</strong>（學習物件導向設計、例外處理、單元測試），R 則專注於純統計分析與圖表繪製。</li>
</ol>
`;
    }

    // Default Fallback Response
    return `
<h3>👋 收到你的諮詢！</h3>
<p>你問了：「<em>${userMessage}</em>」</p>
<p>由於目前处于<strong>本機診斷模式</strong>，我無法做深度的語意理解。但我建議你可以點選下方的<strong>快速諮詢按鈕</strong>，我將為你分析：</p>
<ul>
  <li><strong>統計學理論</strong>如何跟 <strong>Python / R 程式</strong>結合。</li>
  <li>從現有的 SQL/爬蟲技能，如何一步步走到<strong>資料工程 (Data Engineering)</strong>。</li>
  <li>如何把<strong>個體/總體經濟、投資學</strong>觀念做成實用的爬蟲與資料庫專案。</li>
</ul>
<p><em>💡 提示：點擊右上角的「<strong>API 設定</strong>」並填入 Gemini API Key，即可解鎖無限 AI 對話功能，向我詢問任何程式或專題細節喔！</em></p>
`;
  }

  getCategoryName(cat) {
    const names = {
      'statistics': '統計與數學',
      'economics': '經濟與財金',
      'programming': '程式與資工',
      'data_engineering': '資料工程'
    };
    return names[cat] || cat;
  }

  getStatusName(status) {
    const names = {
      'mastered': '已掌握 (Mastered)',
      'learning': '學習中 (Learning)',
      'planned': '計畫中 (Planned)'
    };
    return names[status] || status;
  }

  /**
   * Helper to format markdown bold and lists to HTML
   */
  markdownToHtml(md) {
    let html = md;
    
    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Headings
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^#### (.*?)$/gm, '<h4>$1</h4>');
    html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
    
    // Bullet points (simple replacement)
    html = html.replace(/^\s*-\s*(.*?)$/gm, '<li>$1</li>');
    // Group adjacent <li> into <ul>
    html = html.replace(/(<li>.*?<\/li>)+/gs, match => `<ul>${match}</ul>`);
    
    // Numbered list
    html = html.replace(/^\s*\d+\.\s*(.*?)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*?<\/li>)+/gs, match => `<ol>${match}</ol>`);
    
    // Line breaks
    html = html.replace(/\n/g, '<br>');
    
    // Clean up empty lines or double breaks
    html = html.replace(/(<br>){2,}/g, '<br><br>');
    
    return html;
  }
}

// Export instance
window.skillAssistant = new SkillAssistant();
