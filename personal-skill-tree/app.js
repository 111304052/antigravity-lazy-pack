/**
 * SkillPulse Main Application Logic
 * Manages State, SVG Drawing, Zoom/Pan, Event Handling, and Modals
 */

// Default Seed Data
const DEFAULT_SKILLS = [
  // Statistics & Math
  {
    id: "probability",
    label: "機率論",
    category: "statistics",
    status: "mastered",
    description: "掌握隨機變數、機率密度函數、常見機率分佈（常態、二項、卜瓦松分佈）、期望值、變異數及大數法則、中央極限定理等理論基礎。",
    x: 80,
    y: 160,
    links: []
  },
  {
    id: "mathematical_statistics",
    label: "數理統計",
    category: "statistics",
    status: "mastered",
    description: "深入理解估計理論（最大概似估計 MLE、點估計、區間估計評估）、假設檢定（虛無假說、對立假說、信賴區間、P值與檢定力分析）與無偏性檢驗。",
    x: 80,
    y: 360,
    links: ["probability"]
  },

  // Economics & Finance
  {
    id: "microeconomics",
    label: "個體經濟學",
    category: "economics",
    status: "mastered",
    description: "理解消費者選擇理論、生產與成本分析、市場結構（完全競爭、獨占、寡頭壟斷）以及一般均衡分析。",
    x: 340,
    y: 120,
    links: []
  },
  {
    id: "macroeconomics",
    label: "總體經濟學",
    category: "economics",
    status: "mastered",
    description: "理解國民所得衡量（GDP）、IS-LM 模型、AD-AS 總合供需模型、通貨膨脹與失業率關係，以及中央銀行貨幣政策與政府財政政策影響。",
    x: 340,
    y: 260,
    links: []
  },
  {
    id: "investment",
    label: "投資學",
    category: "economics",
    status: "mastered",
    description: "掌握證券評價、馬可維茲現代投資組合理論 (MPT)、資產定價模型 (CAPM)、衍生性金融商品（選擇權、期貨）評價及有效市場假說 (EMH)。",
    x: 340,
    y: 430,
    links: ["microeconomics", "macroeconomics"]
  },

  // Programming & CS
  {
    id: "python",
    label: "Python 數據分析",
    category: "programming",
    status: "learning",
    description: "掌握 Python 基礎語法與物件導向程式設計，熟練運用數據分析套件（NumPy 進行矩陣運算、pandas 進行資料清洗整理、matplotlib/seaborn 進行數據視覺化）。",
    x: 600,
    y: 100,
    links: []
  },
  {
    id: "r_lang",
    label: "R 語言與統計計算",
    category: "programming",
    status: "mastered",
    description: "熟練使用 R 語言進行統計分析、向量化計算。精通 tidyverse 家族（dplyr, tidyr）進行資料操弄，以及 ggplot2 繪製高水準統計圖表，能編寫機率模擬演算法。",
    x: 600,
    y: 220,
    links: []
  },
  {
    id: "git",
    label: "Git 版本控制",
    category: "programming",
    status: "learning",
    description: "學習版本控制核心觀念與指令（clone, add, commit, push, pull），理解分支管理（branch, merge, checkout）及 GitHub 遠端儲存庫與多人協作流程。",
    x: 600,
    y: 340,
    links: ["python"]
  },
  {
    id: "web_design",
    label: "網頁爬蟲與設計",
    category: "programming",
    status: "learning",
    description: "學習 HTML5、CSS3 與 JavaScript 前端網頁基礎排版與動態邏輯。使用 Python 寫爬蟲，利用 requests、BeautifulSoup 爬取靜態網頁，並學習 Selenium 處理動態 JavaScript 渲染網頁。",
    x: 600,
    y: 480,
    links: ["python"]
  },

  // Data Engineering (DE)
  {
    id: "sql",
    label: "SQL 與資料庫開發",
    category: "data_engineering",
    status: "learning",
    description: "學習關聯式資料庫設計（ER model、Schema、欄位型態），編寫 SQL 語法進行多表關聯（JOIN）、資料聚合（GROUP BY）及複雜子查詢，熟悉 SQLite / PostgreSQL 操作。",
    x: 880,
    y: 200,
    links: ["python"]
  },
  {
    id: "etl_pipelines",
    label: "ETL 資料管道與排程",
    category: "data_engineering",
    status: "planned",
    description: "學習整合多個資料來源（API、網頁爬蟲、資料庫），設計自動化萃取（Extract）、清洗轉換（Transform）與載入（Load）流程，並使用 Apache Airflow 進行排程監控。",
    x: 880,
    y: 380,
    links: ["sql", "web_design"]
  },
  {
    id: "big_data",
    label: "大數據運算 (Spark)",
    category: "data_engineering",
    status: "planned",
    description: "計畫學習 Apache Spark 技術，利用 PySpark 編寫分佈式計算任務，以應對 TB 等級的大規模資料集合與統計分析。",
    x: 880,
    y: 540,
    links: ["etl_pipelines"]
  },
  {
    id: "cloud_platforms",
    label: "雲端數據平台 (GCP)",
    category: "data_engineering",
    status: "planned",
    description: "計畫在 Google Cloud Platform (GCP) 上部署資料管道，學習 BigQuery 雲端資料倉庫、Cloud Functions 無伺服器運算及 Cloud Storage 的整合應用。",
    x: 880,
    y: 690,
    links: ["etl_pipelines"]
  }
];

class SkillTreeApp {
  constructor() {
    this.skills = [];
    this.activeNodeId = null;
    
    // Zoom and Pan State
    this.zoom = { x: 50, y: 30, scale: 0.9 };
    this.isDraggingCanvas = false;
    this.dragStart = { x: 0, y: 0 };
    
    // Node Dragging State
    this.activeDragNodeId = null;
    this.dragged = false; // Check if click or drag
    this.dragNodeOffset = { x: 0, y: 0 };

    // Node Dimensions
    this.nodeWidth = 180;
    this.nodeHeight = 50;

    // DOM cache
    this.svg = document.getElementById('skill-tree-svg');
    this.viewport = document.getElementById('svg-viewport');
    this.linksGroup = document.getElementById('links-group');
    this.nodesGroup = document.getElementById('nodes-group');
    this.canvasContainer = document.getElementById('canvas-container');

    this.init();
  }

  init() {
    this.loadState();
    this.renderStats();
    this.renderTree();
    this.applyZoom();
    this.setupEventListeners();
    this.setupModals();
    this.setupAssistant();
    this.checkApiStatus();
  }

  // Load from local storage or fallback to defaults
  loadState() {
    const data = localStorage.getItem('skillpulse_data');
    if (data) {
      try {
        this.skills = JSON.parse(data);
      } catch (e) {
        console.error("Error parsing stored data, resetting to default", e);
        this.skills = JSON.parse(JSON.stringify(DEFAULT_SKILLS));
        this.saveState();
      }
    } else {
      this.skills = JSON.parse(JSON.stringify(DEFAULT_SKILLS));
      this.saveState();
    }
  }

  saveState() {
    localStorage.setItem('skillpulse_data', JSON.stringify(this.skills));
    this.renderStats();
  }

  renderStats() {
    const stats = { mastered: 0, learning: 0, planned: 0 };
    this.skills.forEach(s => {
      if (stats[s.status] !== undefined) {
        stats[s.status]++;
      }
    });

    document.getElementById('stats-mastered').innerText = stats.mastered;
    document.getElementById('stats-learning').innerText = stats.learning;
    document.getElementById('stats-planned').innerText = stats.planned;
  }

  // Render nodes and links into SVG
  renderTree() {
    this.nodesGroup.innerHTML = '';
    this.linksGroup.innerHTML = '';

    if (this.skills.length === 0) {
      document.getElementById('canvas-empty-state').classList.remove('hidden');
      return;
    } else {
      document.getElementById('canvas-empty-state').classList.add('hidden');
    }

    // 1. Draw Links (connections)
    this.skills.forEach(node => {
      if (node.links && node.links.length > 0) {
        node.links.forEach(prereqId => {
          const prereqNode = this.skills.find(s => s.id === prereqId);
          if (prereqNode) {
            this.drawLink(prereqNode, node);
          }
        });
      }
    });

    // 2. Draw Nodes
    this.skills.forEach(node => {
      this.drawNode(node);
    });
  }

  // Draw a cubic bezier curve connection
  drawLink(parent, child) {
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    
    // Output port: middle of parent right edge
    const outX = parent.x + this.nodeWidth;
    const outY = parent.y + this.nodeHeight / 2;
    
    // Input port: middle of child left edge
    const inX = child.x;
    const inY = child.y + this.nodeHeight / 2;
    
    // Control points for smooth horizontal S-curve
    const dx = Math.abs(inX - outX) * 0.4;
    const cp1X = outX + dx;
    const cp1Y = outY;
    const cp2X = inX - dx;
    const cp2Y = inY;
    
    const d = `M ${outX} ${outY} C ${cp1X} ${cp1Y}, ${cp2X} ${cp2Y}, ${inX} ${inY}`;
    
    path.setAttribute("d", d);
    path.setAttribute("class", `svg-link link-from-${parent.id} link-to-${child.id}`);
    
    // Highlight if selected
    if (this.activeNodeId === parent.id) {
      path.classList.add('highlight');
    } else if (this.activeNodeId === child.id) {
      path.classList.add('dependent-highlight');
    }

    this.linksGroup.appendChild(path);
  }

  // Draw node group with rectangles, status dots, and text
  drawNode(node) {
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    g.setAttribute("class", `svg-node category-${node.category} status-${node.status}`);
    g.setAttribute("transform", `translate(${node.x}, ${node.y})`);
    g.setAttribute("data-id", node.id);

    if (this.activeNodeId === node.id) {
      g.classList.add('active');
    }

    // Outer Rectangle Card
    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("width", this.nodeWidth);
    rect.setAttribute("height", this.nodeHeight);
    rect.setAttribute("class", "svg-node-rect");
    g.appendChild(rect);

    // Color Accent Stripe (Left edge of node)
    const stripe = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    stripe.setAttribute("width", "5");
    stripe.setAttribute("height", this.nodeHeight - 2);
    stripe.setAttribute("x", "1");
    stripe.setAttribute("y", "1");
    stripe.setAttribute("fill", `var(--color-${node.category})`);
    stripe.setAttribute("rx", "2");
    stripe.setAttribute("ry", "2");
    g.appendChild(stripe);

    // Text label
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", "20");
    text.setAttribute("y", "29");
    text.setAttribute("class", "svg-node-text");
    text.textContent = node.label;
    g.appendChild(text);

    // Status Indicator Dot (Top Right)
    const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    dot.setAttribute("cx", this.nodeWidth - 15);
    dot.setAttribute("cy", this.nodeHeight / 2);
    dot.setAttribute("r", "5");
    dot.setAttribute("class", "svg-node-status-dot");
    g.appendChild(dot);

    // Add interactivity to the node
    g.addEventListener('mousedown', (e) => this.handleNodeMouseDown(e, node));
    g.addEventListener('click', (e) => this.handleNodeClick(e, node));

    this.nodesGroup.appendChild(g);
  }

  applyZoom() {
    this.viewport.setAttribute("transform", `translate(${this.zoom.x}, ${this.zoom.y}) scale(${this.zoom.scale})`);
  }

  // Transform page coordinates to SVG local space
  getTransformedCoords(e) {
    const rect = this.svg.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    return {
      x: (mouseX - this.zoom.x) / this.zoom.scale,
      y: (mouseY - this.zoom.y) / this.zoom.scale
    };
  }

  // Event Listeners
  setupEventListeners() {
    // 1. Zoom and Pan Controls
    document.getElementById('btn-zoom-in').addEventListener('click', () => {
      this.zoom.scale = Math.min(3.0, this.zoom.scale + 0.15);
      this.applyZoom();
    });
    
    document.getElementById('btn-zoom-out').addEventListener('click', () => {
      this.zoom.scale = Math.max(0.3, this.zoom.scale - 0.15);
      this.applyZoom();
    });
    
    document.getElementById('btn-zoom-reset').addEventListener('click', () => {
      this.zoom = { x: 50, y: 30, scale: 0.9 };
      this.applyZoom();
    });

    // 2. SVG Wheel Zoom
    this.svg.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = 0.05;
      const delta = e.deltaY < 0 ? 1 : -1;
      
      const prevScale = this.zoom.scale;
      this.zoom.scale = Math.min(3.0, Math.max(0.3, this.zoom.scale + delta * zoomFactor));
      
      // Keep zoom center relative to mouse position
      const rect = this.svg.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;
      
      this.zoom.x = mouseX - (mouseX - this.zoom.x) * (this.zoom.scale / prevScale);
      this.zoom.y = mouseY - (mouseY - this.zoom.y) * (this.zoom.scale / prevScale);

      this.applyZoom();
    });

    // 3. Canvas Panning
    this.svg.addEventListener('mousedown', (e) => {
      // Ignore right clicks or if we click a node
      if (e.button !== 0 || e.target.closest('.svg-node')) return;
      
      this.isDraggingCanvas = true;
      this.dragStart.x = e.clientX - this.zoom.x;
      this.dragStart.y = e.clientY - this.zoom.y;
      this.svg.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', (e) => {
      // Node Dragging
      if (this.activeDragNodeId) {
        this.dragged = true;
        const coords = this.getTransformedCoords(e);
        const node = this.skills.find(s => s.id === this.activeDragNodeId);
        if (node) {
          node.x = Math.round(coords.x - this.dragNodeOffset.x);
          node.y = Math.round(coords.y - this.dragNodeOffset.y);
          this.renderTree(); // Dynamically draw paths
        }
        return;
      }

      // Canvas panning
      if (this.isDraggingCanvas) {
        this.zoom.x = e.clientX - this.dragStart.x;
        this.zoom.y = e.clientY - this.dragStart.y;
        this.applyZoom();
      }
    });

    window.addEventListener('mouseup', () => {
      if (this.activeDragNodeId) {
        this.activeDragNodeId = null;
        this.saveState();
      }
      if (this.isDraggingCanvas) {
        this.isDraggingCanvas = false;
        this.svg.style.cursor = 'grab';
      }
    });

    // Details Panel close button
    document.getElementById('btn-close-details').addEventListener('click', () => {
      this.deselectNode();
    });

    // Node state edits directly from select box in details panel
    document.getElementById('details-status').addEventListener('change', (e) => {
      if (this.activeNodeId) {
        const node = this.skills.find(s => s.id === this.activeNodeId);
        if (node) {
          node.status = e.target.value;
          this.saveState();
          this.renderTree();
        }
      }
    });
  }

  // Node Dragging MouseDown
  handleNodeMouseDown(e, node) {
    if (e.button !== 0) return; // Left click only
    e.stopPropagation(); // Don't trigger canvas drag
    
    this.activeDragNodeId = node.id;
    this.dragged = false;

    const coords = this.getTransformedCoords(e);
    this.dragNodeOffset.x = coords.x - node.x;
    this.dragNodeOffset.y = coords.y - node.y;
  }

  // Node Select Click
  handleNodeClick(e, node) {
    e.stopPropagation();
    if (this.dragged) return; // Ignore clicks that were drags

    this.selectNode(node);
  }

  selectNode(node) {
    this.activeNodeId = node.id;
    this.renderTree(); // Highlighting connected paths

    // Populate and slide in Details Panel
    document.getElementById('details-title').innerText = node.label;
    
    const catTag = document.getElementById('details-category');
    catTag.innerText = window.skillAssistant.getCategoryName(node.category);
    catTag.className = `info-value category-tag tag-${node.category}`;
    
    document.getElementById('details-status').value = node.status;
    document.getElementById('details-desc').innerHTML = node.description ? node.description.replace(/\n/g, '<br>') : '尚未填寫技能描述。';

    // Set Relations section
    const relsDiv = document.getElementById('details-relations');
    relsDiv.innerHTML = '';

    // 1. Prerequisites (parents)
    if (node.links && node.links.length > 0) {
      const parentLabel = document.createElement('div');
      parentLabel.className = 'relation-label';
      parentLabel.innerText = '前置技能 (Prerequisites)：';
      relsDiv.appendChild(parentLabel);

      const badges = document.createElement('div');
      badges.className = 'relation-badges';
      node.links.forEach(pId => {
        const pNode = this.skills.find(s => s.id === pId);
        if (pNode) {
          const badge = document.createElement('span');
          badge.className = 'relation-badge';
          badge.innerText = pNode.label;
          badge.addEventListener('click', () => this.selectNode(pNode));
          badges.appendChild(badge);
        }
      });
      relsDiv.appendChild(badges);
    }

    // 2. Dependent skills (children)
    const children = this.skills.filter(s => s.links && s.links.includes(node.id));
    if (children.length > 0) {
      const childLabel = document.createElement('div');
      childLabel.className = 'relation-label';
      childLabel.style.marginTop = '10px';
      childLabel.innerText = '衍生技能 (Unlocks)：';
      relsDiv.appendChild(childLabel);

      const badges = document.createElement('div');
      badges.className = 'relation-badges';
      children.forEach(cNode => {
        const badge = document.createElement('span');
        badge.className = 'relation-badge';
        badge.innerText = cNode.label;
        badge.addEventListener('click', () => this.selectNode(cNode));
        badges.appendChild(badge);
      });
      relsDiv.appendChild(badges);
    }

    document.getElementById('node-details-panel').classList.remove('hidden');
  }

  deselectNode() {
    this.activeNodeId = null;
    document.getElementById('node-details-panel').classList.add('hidden');
    this.renderTree();
  }

  // Setup modals (Add/Edit Node, API Key setup, Backup management)
  setupModals() {
    const modals = {
      'btn-api-config': 'modal-api',
      'btn-import-export': 'modal-data',
      'btn-add-skill': 'modal-node-editor'
    };

    // Open Modals
    Object.keys(modals).forEach(btnId => {
      const btn = document.getElementById(btnId);
      const modalId = modals[btnId];
      btn.addEventListener('click', () => {
        if (modalId === 'modal-node-editor') {
          this.openNodeEditor();
        } else {
          this.showModal(modalId);
        }
      });
    });

    // Close Modals (X buttons and cancels)
    document.querySelectorAll('.modal-close').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const modalId = btn.getAttribute('data-close');
        this.hideModal(modalId);
      });
    });

    // Click outside to close
    document.querySelectorAll('.modal').forEach(modal => {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          this.hideModal(modal.id);
        }
      });
    });

    // Save API key
    document.getElementById('btn-save-api').addEventListener('click', () => {
      const key = document.getElementById('api-key-input').value.trim();
      window.skillAssistant.setApiKey(key);
      this.checkApiStatus();
      this.hideModal('modal-api');
      this.addSystemMessage(`🔑 **API 金鑰設定成功！**\n已為您切換至 **Gemini 線上智慧諮詢模式**。現在您可以詢問任何深入的學習問題囉！`);
    });

    document.getElementById('btn-clear-api').addEventListener('click', () => {
      document.getElementById('api-key-input').value = '';
      window.skillAssistant.setApiKey(null);
      this.checkApiStatus();
      this.hideModal('modal-api');
      this.addSystemMessage(`ℹ️ **API 金鑰已清除。**\n系統已切換回 **本機診斷模式**。`);
    });

    // Data Management Modals buttons
    // 1. Export JSON
    document.getElementById('btn-export-json').addEventListener('click', () => {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.skills, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", "skillpulse_tree_backup.json");
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    });

    // 2. Import JSON
    const fileInput = document.getElementById('import-file-input');
    const importTriggerBtn = document.getElementById('btn-trigger-import');
    const fileNameSpan = document.getElementById('import-file-name');
    const importConfirmBtn = document.getElementById('btn-import-json');

    importTriggerBtn.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', () => {
      if (fileInput.files.length > 0) {
        fileNameSpan.innerText = fileInput.files[0].name;
        importConfirmBtn.removeAttribute('disabled');
      } else {
        fileNameSpan.innerText = '未選擇檔案';
        importConfirmBtn.setAttribute('disabled', 'true');
      }
    });

    importConfirmBtn.addEventListener('click', () => {
      const file = fileInput.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const importedData = JSON.parse(e.target.result);
          if (Array.isArray(importedData)) {
            // Validate basic structure
            const isValid = importedData.every(item => item.id && item.label && item.category && item.status);
            if (isValid) {
              this.skills = importedData;
              this.saveState();
              this.renderTree();
              this.deselectNode();
              this.hideModal('modal-data');
              this.addSystemMessage(`📥 **技能樹還原成功！**\n已從備份檔案載入新的技能架構。`);
            } else {
              alert('JSON 格式無效：必須是包含技能節點資訊的陣列！');
            }
          } else {
            alert('JSON 格式無效：根節點必須是陣列！');
          }
        } catch (err) {
          alert('解析 JSON 檔案失敗！');
        }
      };
      reader.readAsText(file);
    });

    // Reset default
    document.getElementById('btn-reset-default').addEventListener('click', () => {
      if (confirm('確定要還原成預設技能樹嗎？這將刪除您所有自訂的節點與編輯紀錄！')) {
        this.skills = JSON.parse(JSON.stringify(DEFAULT_SKILLS));
        this.saveState();
        this.renderTree();
        this.deselectNode();
        this.hideModal('modal-data');
        this.addSystemMessage(`🔄 **技能樹已還原為預設配置**。`);
      }
    });

    // Edit/Add Node saving button
    document.getElementById('btn-save-node').addEventListener('click', () => {
      this.saveNodeFromEditor();
    });

    // Node edit actions inside details panel
    document.getElementById('btn-edit-node').addEventListener('click', () => {
      if (this.activeNodeId) {
        const node = this.skills.find(s => s.id === this.activeNodeId);
        if (node) {
          this.openNodeEditor(node);
        }
      }
    });

    document.getElementById('btn-delete-node').addEventListener('click', () => {
      if (this.activeNodeId) {
        const node = this.skills.find(s => s.id === this.activeNodeId);
        if (node) {
          if (confirm(`確定要刪除技能「${node.label}」嗎？這也會移除其他技能中指向此節點的前置連結。`)) {
            const deleteId = node.id;
            
            // Remove node
            this.skills = this.skills.filter(s => s.id !== deleteId);
            
            // Remove from other nodes' links lists
            this.skills.forEach(s => {
              if (s.links && s.links.includes(deleteId)) {
                s.links = s.links.filter(pId => pId !== deleteId);
              }
            });

            this.saveState();
            this.deselectNode();
            this.renderTree();
            this.addSystemMessage(`🗑️ 已刪除技能節點 **${node.label}**。`);
          }
        }
      }
    });
  }

  showModal(id) {
    document.getElementById(id).classList.remove('hidden');
    if (id === 'modal-api') {
      const key = localStorage.getItem('gemini_api_key') || '';
      document.getElementById('api-key-input').value = key;
    }
  }

  hideModal(id) {
    document.getElementById(id).classList.add('hidden');
  }

  checkApiStatus() {
    const badge = document.getElementById('api-status-badge');
    if (window.skillAssistant.hasApiKey()) {
      badge.innerText = 'Gemini 智慧模式';
      badge.className = 'api-status gemini';
    } else {
      badge.innerText = '本機診斷模式';
      badge.className = 'api-status local';
    }
  }

  // Open the add/edit form
  openNodeEditor(node = null) {
    this.showModal('modal-node-editor');
    const form = document.getElementById('node-editor-form');
    form.reset();

    const titleEl = document.getElementById('editor-modal-title');
    const idInput = document.getElementById('edit-node-id');
    const labelInput = document.getElementById('edit-node-label');
    const catSelect = document.getElementById('edit-node-category');
    const statusSelect = document.getElementById('edit-node-status');
    const descTextarea = document.getElementById('edit-node-desc');
    const xInput = document.getElementById('edit-node-x');
    const yInput = document.getElementById('edit-node-y');

    // Populate prerequisite checkboxes
    const prereqContainer = document.getElementById('prerequisites-list-container');
    prereqContainer.innerHTML = '';

    // List all OTHER nodes as possible prerequisites
    const possiblePrereqs = this.skills.filter(s => !node || s.id !== node.id);
    
    if (possiblePrereqs.length === 0) {
      prereqContainer.innerHTML = '<div style="color: var(--text-muted); font-size:11px; padding: 4px;">目前沒有其他節點可以連結</div>';
    } else {
      possiblePrereqs.forEach(s => {
        const item = document.createElement('label');
        item.className = 'checkbox-item';
        
        const cb = document.createElement('input');
        cb.type = 'checkbox';
        cb.value = s.id;
        if (node && node.links && node.links.includes(s.id)) {
          cb.checked = true;
        }
        
        item.appendChild(cb);
        
        // Color dot represent category
        const dot = document.createElement('span');
        dot.style.display = 'inline-block';
        dot.style.width = '8px';
        dot.style.height = '8px';
        dot.style.borderRadius = '50%';
        dot.style.backgroundColor = `var(--color-${s.category})`;
        item.appendChild(dot);

        const spanText = document.createElement('span');
        spanText.innerText = s.label;
        item.appendChild(spanText);
        
        prereqContainer.appendChild(item);
      });
    }

    if (node) {
      // Editing Mode
      titleEl.innerText = `編輯技能節點: ${node.label}`;
      idInput.value = node.id;
      labelInput.value = node.label;
      catSelect.value = node.category;
      statusSelect.value = node.status;
      descTextarea.value = node.description || '';
      xInput.value = node.x;
      yInput.value = node.y;
    } else {
      // Adding Mode
      titleEl.innerText = '新增技能節點';
      idInput.value = '';
      xInput.value = '';
      yInput.value = '';
    }
  }

  saveNodeFromEditor() {
    const id = document.getElementById('edit-node-id').value;
    const label = document.getElementById('edit-node-label').value.trim();
    const category = document.getElementById('edit-node-category').value;
    const status = document.getElementById('edit-node-status').value;
    const description = document.getElementById('edit-node-desc').value.trim();
    
    let x = parseInt(document.getElementById('edit-node-x').value);
    let y = parseInt(document.getElementById('edit-node-y').value);

    if (!label) {
      alert('請填寫技能名稱！');
      return;
    }

    // Get checked prerequisites
    const checkedCheckboxes = document.querySelectorAll('#prerequisites-list-container input[type="checkbox"]:checked');
    const links = Array.from(checkedCheckboxes).map(cb => cb.value);

    if (id) {
      // Update Node
      const node = this.skills.find(s => s.id === id);
      if (node) {
        node.label = label;
        node.category = category;
        node.status = status;
        node.description = description;
        node.links = links;
        if (!isNaN(x)) node.x = x;
        if (!isNaN(y)) node.y = y;
        
        this.saveState();
        this.deselectNode();
        this.renderTree();
        this.hideModal('modal-node-editor');
        this.addSystemMessage(`✏️ 已更新技能節點 **${label}**。`);
      }
    } else {
      // Create Node
      // Helper: Assign coordinate based on category column if x or y is empty
      if (isNaN(x) || isNaN(y)) {
        const columns = {
          'statistics': 100,
          'economics': 350,
          'programming': 600,
          'data_engineering': 880
        };
        x = columns[category] || 100;
        
        // Find maximum Y in this category
        const sameCategoryNodes = this.skills.filter(s => s.category === category);
        if (sameCategoryNodes.length > 0) {
          const maxY = Math.max(...sameCategoryNodes.map(s => s.y));
          y = maxY + 120;
        } else {
          y = 150;
        }
      }

      // Generate a unique ID from label
      const newId = 'node_' + Date.now();
      
      const newNode = {
        id: newId,
        label,
        category,
        status,
        description,
        x,
        y,
        links
      };

      this.skills.push(newNode);
      this.saveState();
      this.renderTree();
      this.hideModal('modal-node-editor');
      this.addSystemMessage(`➕ 已新增技能節點 **${label}** 到 *${window.skillAssistant.getCategoryName(category)}* 類別。`);
      
      // Auto select the new node
      this.selectNode(newNode);
    }
  }

  // Setup Chat Assistant UI
  setupAssistant() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const messageText = chatInput.value.trim();
      if (!messageText) return;

      chatInput.value = '';
      await this.handleUserQuery(messageText);
    });

    // Quick prompts triggers
    document.querySelectorAll('.quick-prompt-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const text = btn.getAttribute('data-prompt');
        await this.handleUserQuery(text);
      });
    });
  }

  async handleUserQuery(text) {
    // Add user message
    this.addUserMessage(text);
    
    // Add typing indicator
    const typingIndicator = this.addTypingIndicator();
    
    try {
      // Get AI response
      const htmlResponse = await window.skillAssistant.getResponse(text, this.skills);
      typingIndicator.remove();
      this.addSystemMessage(htmlResponse, true); // Raw HTML output
    } catch (err) {
      console.error(err);
      typingIndicator.remove();
      this.addSystemMessage(`❌ **發生錯誤：** 無法獲取回覆。請確認您的網路連線或 API 金鑰設定。`);
    }
  }

  addUserMessage(text) {
    const chatMessages = document.getElementById('chat-messages');
    
    const div = document.createElement('div');
    div.className = 'message user';
    div.innerHTML = `
      <div class="msg-avatar"><i class="fa-solid fa-user"></i></div>
      <div class="msg-content">
        <p>${this.escapeHtml(text)}</p>
      </div>
    `;
    
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  addSystemMessage(content, isHtml = false) {
    const chatMessages = document.getElementById('chat-messages');
    
    const div = document.createElement('div');
    div.className = 'message system';
    
    const contentHtml = isHtml ? content : window.skillAssistant.markdownToHtml(content);
    
    div.innerHTML = `
      <div class="msg-avatar"><i class="fa-solid fa-user-astronaut"></i></div>
      <div class="msg-content">
        ${contentHtml}
      </div>
    `;
    
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  addTypingIndicator() {
    const chatMessages = document.getElementById('chat-messages');
    
    const div = document.createElement('div');
    div.className = 'message system';
    div.innerHTML = `
      <div class="msg-avatar"><i class="fa-solid fa-user-astronaut"></i></div>
      <div class="msg-content">
        <div class="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    `;
    
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return div;
  }

  escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
  }
}

// Instantiate on load
window.addEventListener('DOMContentLoaded', () => {
  window.skillTreeApp = new SkillTreeApp();
});
