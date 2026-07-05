import sys
import subprocess
import os

# 1. 自動安裝 reportlab
try:
    import reportlab
except ImportError:
    print("未偵測到 reportlab，正在進行安裝...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    print("reportlab 安裝完成。")

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

# 2. 註冊 Windows 系統的微軟正黑體以支援中文
font_path = "C:/Windows/Fonts/msjh.ttc"  # 微軟正黑體
font_bold_path = "C:/Windows/Fonts/msjhbd.ttc"  # 微軟正黑體 Bold

if not os.path.exists(font_path):
    # 如果找不到，嘗試使用系統內的其他路徑或預設
    font_path = "C:/Windows/Fonts/msjh.ttf"
if not os.path.exists(font_bold_path):
    font_bold_path = font_path

try:
    pdfmetrics.registerFont(TTFont('MSJH', font_path))
    pdfmetrics.registerFont(TTFont('MSJH_BD', font_bold_path))
    print("已成功註冊微軟正黑體。")
except Exception as e:
    print(f"註冊微軟正黑體失敗，使用系統預設字型 (可能會顯示亂碼): {e}")
    # 註冊預設字型
    pdfmetrics.registerFont(TTFont('MSJH', 'Helvetica'))
    pdfmetrics.registerFont(TTFont('MSJH_BD', 'Helvetica-Bold'))

# 3. 簡報內容與繪製類別
class PresentationGenerator:
    def __init__(self, filename="financial_agent_presentation.pdf"):
        self.filename = filename
        # 橫式 Letter 尺寸為 792 x 612 點 (Points)
        self.width, self.height = landscape(letter)
        self.c = canvas.Canvas(filename, pagesize=(self.width, self.height))
        
        # 配色方案 (現代深藍金融風)
        self.c_bg = colors.HexColor("#0F172A")       # 深藍灰色背景 (封面)
        self.c_white = colors.HexColor("#FFFFFF")
        self.c_primary = colors.HexColor("#1E293B")   # 主文字 (Slate 800)
        self.c_accent = colors.HexColor("#2563EB")    # 強調藍 (Blue 600)
        self.c_secondary = colors.HexColor("#64748B") # 次要文字 (Slate 500)
        self.c_light_bg = colors.HexColor("#F8FAFC")  # 內頁背景 (Slate 50)
        self.c_card_bg = colors.HexColor("#FFFFFF")   # 卡片背景

    def draw_cover(self):
        # 繪製深色背景
        self.c.setFillColor(self.c_bg)
        self.c.rect(0, 0, self.width, self.height, fill=True, stroke=False)
        
        # 繪製裝飾幾何圖形
        self.c.setFillColor(self.c_accent)
        self.c.rect(0, 0, 15, self.height, fill=True, stroke=False)
        self.c.circle(self.width - 50, self.height - 50, 100, fill=True, stroke=False)
        self.c.setFillColor(colors.HexColor("#1E293B"))
        self.c.circle(self.width - 50, self.height - 50, 80, fill=True, stroke=False)
        
        # 標題
        self.c.setFillColor(self.c_white)
        self.c.setFont("MSJH_BD", 32)
        self.c.drawString(60, 320, "金融 AI Agent 應用藍圖")
        
        # 副標題
        self.c.setFont("MSJH", 18)
        self.c.setFillColor(colors.HexColor("#94A3B8"))
        self.c.drawString(60, 260, "從零打造自動化風險分析與個人化理財助理")
        
        # 底部資訊
        self.c.setFont("MSJH", 12)
        self.c.setFillColor(colors.HexColor("#64748B"))
        self.c.drawString(60, 80, "報告對象：金融業創新研發團隊")
        self.c.drawString(60, 55, "生成時間：2026 年 7 月")
        
        self.c.showPage()

    def draw_slide_header(self, title_text, category="FINANCIAL AI AGENT"):
        # 背景
        self.c.setFillColor(self.c_light_bg)
        self.c.rect(0, 0, self.width, self.height, fill=True, stroke=False)
        
        # 頁首藍色條
        self.c.setFillColor(self.c_accent)
        self.c.rect(0, self.height - 8, self.width, 8, fill=True, stroke=False)
        
        # 頁首類別文字
        self.c.setFont("MSJH_BD", 9)
        self.c.setFillColor(self.c_accent)
        self.c.drawString(50, self.height - 35, category)
        
        # 頁首大標題
        self.c.setFont("MSJH_BD", 22)
        self.c.setFillColor(self.c_primary)
        self.c.drawString(50, self.height - 65, title_text)
        
        # 頁首分割線
        self.c.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.c.setLineWidth(1)
        self.c.line(50, self.height - 75, self.width - 50, self.height - 75)

    def draw_slide_footer(self, page_num):
        # 頁尾線
        self.c.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.c.setLineWidth(0.5)
        self.c.line(50, 45, self.width - 50, 45)
        
        # 頁尾版權文字與頁碼
        self.c.setFont("MSJH", 9)
        self.c.setFillColor(self.c_secondary)
        self.c.drawString(50, 25, "金融 AI Agent 應用藍圖簡報")
        self.c.drawRightString(self.width - 50, 25, f"Page {page_num} of 7")

    def draw_card(self, x, y, w, h, title, lines):
        # 繪製卡片背景與陰影
        self.c.setFillColor(colors.HexColor("#F1F5F9"))
        self.c.rect(x+2, y-2, w, h, fill=True, stroke=False) # 陰影
        self.c.setFillColor(self.c_card_bg)
        self.c.rect(x, y, w, h, fill=True, stroke=False)
        
        # 左側裝飾條
        self.c.setFillColor(self.c_accent)
        self.c.rect(x, y, 4, h, fill=True, stroke=False)
        
        # 卡片標題
        self.c.setFont("MSJH_BD", 13)
        self.c.setFillColor(self.c_primary)
        self.c.drawString(x + 20, y + h - 25, title)
        
        # 卡片內容
        self.c.setFont("MSJH", 10.5)
        self.c.setFillColor(colors.HexColor("#334155"))
        curr_y = y + h - 50
        for line in lines:
            self.c.drawString(x + 20, curr_y, line)
            curr_y -= 18

    def slide_2(self):
        self.draw_slide_header("AI Agent 在金融業的核心四支柱")
        
        # 繪製四個支柱卡片
        self.draw_card(50, 270, 330, 180, "1. 感知與數據源 (Perception)", [
            "• 多模態輸入：解析文字、語音、財報 PDF",
            "• 即時行情：串接 Yahoo Finance 與 API",
            "• 用戶資產：Open Banking 數據整合",
            "• 外部資訊：輿情新聞即時檢索 (Tavily)"
        ])
        
        self.draw_card(410, 270, 330, 180, "2. 規劃與大腦 (Reasoning & Planning)", [
            "• LLM 核心：任務拆解、策略制定",
            "• 長短期記憶：利用 pgvector 保存上下文",
            "• 確定性流程：使用 LangGraph 繪製狀態圖",
            "• 思考模式：金融鏈思維 (Financial CoT)"
        ])
        
        self.draw_card(50, 70, 330, 180, "3. 工具執行 (Action)", [
            "• 數據計算：Python 量化工具庫 (Scipy, Pandas)",
            "• 帳戶操作：Plaid / 開放銀行交易 API",
            "• 通知引擎：LINE Messaging API 即時推播",
            "• 自動化流：排程與異常消費警示 (n8n)"
        ])
        
        self.draw_card(410, 70, 330, 180, "4. 安全與護欄 (Guardrails)", [
            "• 人機協作：高風險決策必須經過人工確認",
            "• 安全護欄：NeMo Guardrails 防止幻覺與偏誤",
            "• 稽核追蹤：LangSmith 紀錄每一步推理邏輯",
            "• 法規對齊：向量庫即時比對合規指南"
        ])
        
        self.draw_slide_footer(2)
        self.c.showPage()

    def slide_3(self):
        self.draw_slide_header("自動化風險分析：系統架構與流程")
        
        # 繪製流程步驟卡片 (橫向)
        w_box = 150
        h_box = 280
        y_pos = 140
        
        steps = [
            ("第一步：數據採集", ["• 抓取公司 Ticker", "• yfinance 股價行情", "• Tavily 網路輿情", "• RAG 檢索合規文件"], 50),
            ("第二步：量化計算", ["• 波動率估算", "• 最大回撤計算", "• 蒙地卡羅模擬 VaR", "• 資產分配優化"], 225),
            ("第三步：風險評估", ["• LLM 分析指標", "• 比對法規防線", "• 判定信用/市場風險", "• 生成初步分析草稿"], 400),
            ("第四步：人機協作", ["• LangGraph 中斷", "• 暫停流程等待審查", "• 分析師點選核准", "• 修正或直接放行"], 575)
        ]
        
        for title, lines, x in steps:
            self.draw_card(x, y_pos, w_box, h_box, title, lines)
            # 繪製箭頭
            if x < 575:
                self.c.setStrokeColor(self.c_accent)
                self.c.setLineWidth(2)
                self.c.line(x + w_box + 5, y_pos + h_box/2, x + w_box + 20, y_pos + h_box/2)
                self.c.line(x + w_box + 15, y_pos + h_box/2 - 5, x + w_box + 20, y_pos + h_box/2)
                self.c.line(x + w_box + 15, y_pos + h_box/2 + 5, x + w_box + 20, y_pos + h_box/2)

        # 底部重點提示
        self.c.setFont("MSJH_BD", 11)
        self.c.setFillColor(self.c_accent)
        self.c.drawString(50, 80, "關鍵設計：LangGraph 中斷機制 (Interrupt) 確保金融系統具有可控的人機協作閘口。")
        
        self.draw_slide_footer(3)
        self.c.showPage()

    def slide_4(self):
        self.draw_slide_header("自動化風險分析：關鍵工具選型")
        
        self.draw_card(50, 270, 330, 180, "核心框架與量化庫", [
            "• LangGraph：管理多節點有向圖與審核中斷",
            "• FinRobot：金融專用思維鏈模板",
            "• yfinance：獲取免費且快速的市場歷史數據",
            "• PyPortfolioOpt：量化組合優化與風險分析"
        ])
        
        self.draw_card(410, 270, 330, 180, "定性與輿情分析", [
            "• Tavily Search：LLM 專用即時新聞與輿情檢索",
            "• Qdrant / Milvus：向量資料庫，儲存法規守則",
            "• PDF Parser：用於解析複雜的上市公司財報",
            "• Llama Guard：過濾敏感與不合規輸出"
        ])
        
        # 繪製一行文字提示
        self.c.setFont("MSJH", 12)
        self.c.setFillColor(self.c_primary)
        self.c.drawString(50, 180, "開發落地建議：")
        self.c.setFont("MSJH", 10.5)
        self.c.setFillColor(colors.HexColor("#334155"))
        self.c.drawString(50, 155, "1. 快速 PoC 階段：使用 Dify 或 Langflow 可視化搭建，快速連接 OpenAI 與 Yahoo Finance API。")
        self.c.drawString(50, 135, "2. 生產環境階段：轉移至 Python 原始碼，配合 LangGraph 進行嚴密狀態管理，並串接 LangSmith 做稽核。")
        
        self.draw_slide_footer(4)
        self.c.showPage()

    def slide_5(self):
        self.draw_slide_header("個人化理財助理：系統架構與互動")
        
        self.draw_card(50, 270, 330, 180, "用戶資料串接與整合", [
            "• Plaid API：全球主流 Open Banking 整合器",
            "• 台灣開放銀行 API：串接 TSP 平台獲取銀行帳單",
            "• 手動上傳：支援 CSV/圖片 帳單解析與自動分類",
            "• 長期記憶：PostgreSQL 紀錄用戶財務目標"
        ])
        
        self.draw_card(410, 270, 330, 180, "對話前端與主動推播", [
            "• LINE Bot：台灣與亞洲最便利的互動管道",
            "• Next.js Web App：資產佔比與消費趨勢圖表",
            "• 自動化引擎：n8n 監聽預算，主動觸發警告",
            "• 智能回覆：結合用戶記憶，給出定制化理財建議"
        ])
        
        # 繪製互動示意圖文字版
        self.c.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.c.setFillColor(colors.HexColor("#F8FAFC"))
        self.c.rect(50, 80, 690, 120, fill=True, stroke=True)
        
        self.c.setFont("MSJH_BD", 12)
        self.c.setFillColor(self.c_accent)
        self.c.drawString(70, 170, "理財助理核心對話流示例：")
        
        self.c.setFont("MSJH", 10.5)
        self.c.setFillColor(self.c_primary)
        self.c.drawString(70, 145, "用戶：「我今年想存 50 萬買房，我目前的餐飲消費有超標嗎？」")
        self.c.setFillColor(colors.HexColor("#16A34A"))
        self.c.drawString(70, 125, "Agent：「根據長期記憶，您設定了買房目標。我串接 Plaid 發現您本月餐飲已花費 12,000 元，」")
        self.c.drawString(70, 105, "         「超出本月預算的 20%。建議本週減少外食，目前儲存進度已達 15%！」")

        self.draw_slide_footer(5)
        self.c.showPage()

    def slide_6(self):
        self.draw_slide_header("個人化理財助理：關鍵工具選型")
        
        self.draw_card(50, 270, 330, 180, "數據庫與記憶管理", [
            "• PostgreSQL + pgvector：儲存結構化記帳明細",
            "  與對話向量，實現「長期買房/理財目標」記憶",
            "• Redis：極速對話快取，儲存當前 Session 狀態",
            "• Celery：Python 定時任務框架，負責警示發送"
        ])
        
        self.draw_card(410, 270, 330, 180, "管道、前端與自動化", [
            "• LINE Messaging API：提供直覺式 Rich Menu",
            "• Tailwind CSS + Recharts：建置輕量資產 Dashboard",
            "• n8n：低代碼整合 n8n 與 LINE、資料庫、與 LLM",
            "• LangChain Router：判定用戶意圖，決定調用工具"
        ])
        
        # 繪製資安警示
        self.c.setFillColor(colors.HexColor("#FFFBEB"))
        self.c.setStrokeColor(colors.HexColor("#FCD34D"))
        self.c.rect(50, 80, 690, 140, fill=True, stroke=True)
        
        self.c.setFont("MSJH_BD", 11)
        self.c.setFillColor(colors.HexColor("#B45309"))
        self.c.drawString(70, 195, "⚠️ 金融資料隱私與資安合規注意事項：")
        
        self.c.setFont("MSJH", 10)
        self.c.setFillColor(colors.HexColor("#78350F"))
        self.c.drawString(70, 175, "1. 數據去識別化：用戶帳單明細在進入 LLM 前，需進行去敏感 (PII masking) 處理，保護個資。")
        self.c.drawString(70, 155, "2. 授權期限管理：台灣開放銀行 API 與 Plaid 皆有授權期限（如 90-365天），系統需有自動提醒更新授權機制。")
        self.c.drawString(70, 135, "3. 本地化部署：若為大型金融機構，推薦將 LLM 部署在企業私有雲 (On-Premise) 以符合金管會規範。")

        self.draw_slide_footer(6)
        self.c.showPage()

    def slide_7(self):
        self.draw_slide_header("金融 AI Agent 落地實施路線圖 (Roadmap)")
        
        # 繪製三階段 Roadmap 卡片
        w_box = 220
        h_box = 320
        y_pos = 100
        
        self.draw_card(50, y_pos, w_box, h_box, "第一階段：快速 PoC 驗證", [
            "完成時間：1 - 3 週",
            "目標：快速打通核心流程",
            "",
            "1. 使用 Dify 或 LangGraph",
            "   跑通單股市場風險計算。",
            "2. 使用 yfinance 免費數據，",
            "   並放上少數 PDF 政策檔。",
            "3. 串接 LINE Bot 模擬記帳",
            "   與預算設定（假數據）。",
            "4. 進行小範圍內部測試。"
        ])
        
        self.draw_card(285, y_pos, w_box, h_box, "第二階段：人機協作與合規", [
            "完成時間：1 - 2 個月",
            "目標：提升精準度與安全性",
            "",
            "1. 實作 LangGraph 中斷機制，",
            "   建立分析師審查 UI。",
            "2. 引進 pgvector 向量檢索，",
            "   比對完整監理法規庫。",
            "3. 引入數據脫敏機制，",
            "   遮蔽姓名、卡號等 PII。",
            "4. 正式導入 LangSmith 監控。"
        ])
        
        self.draw_card(520, y_pos, w_box, h_box, "第三階段：全面整合部署", [
            "完成時間：3 - 6 個月",
            "目標：正式商用與全面對接",
            "",
            "1. 正式申請 Plaid 生產環境",
            "   金鑰，或與 TSP 業者對接。",
            "2. 將 Agent 核心整合進",
            "   企業內部資料庫 (Postgres)。",
            "3. 串接排程工作流 (n8n/Celery)",
            "   實現主動式預算/風險警示。",
            "4. 部署於金融企業私有雲。"
        ])
        
        self.draw_slide_footer(7)
        self.c.showPage()

    def generate(self):
        self.draw_cover()
        self.slide_2()
        self.slide_3()
        self.slide_4()
        self.slide_5()
        self.slide_6()
        self.slide_7()
        self.c.save()
        print(f"成功生成 PDF 簡報於 {self.filename}")

if __name__ == "__main__":
    generator = PresentationGenerator()
    generator.generate()
