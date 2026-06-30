# -*- coding: utf-8 -*-
import os
import glob
import json
import re
import shutil

# 定義路徑
output_base = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\output\【機器學習2021】(中文版)"
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\【機器學習2021】(中文版)"
input_dir = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\input"

# 1. 清理舊的筆記檔案，防止檔名混雜
if os.path.exists(output_base):
    shutil.rmtree(output_base)
if os.path.exists(obsidian_base):
    shutil.rmtree(obsidian_base)

os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 2. 掃描 input 目錄，提取包含 playlist_index 且屬於目標清單的影片
json_files = glob.glob(os.path.join(input_dir, "*.info.json"))
video_list = []

for fpath in json_files:
    if "video.info.json" in fpath or "PLkNQUBglz8Eyh1xcFYFBOcOEBu1WGoB0p.info.json" in fpath or "PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J.info.json" in fpath:
        continue
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            playlist_id = data.get("playlist_id")
            if playlist_id == "PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J":
                idx = data.get("playlist_index")
                v_id = data.get("id")
                title = data.get("title")
                
                # 如果沒有 idx，嘗試從檔名或 autonumber 推算，這裡強制轉 int
                if idx is not None:
                    idx = int(idx)
                else:
                    idx = 99  # 預設排最後
                    
                video_list.append({
                    "index": idx,
                    "id": v_id,
                    "title": title
                })
    except Exception as e:
        print(f"Error parsing {fpath}: {e}")

# 依據播放清單 Index 升冪排序
video_list.sort(key=lambda x: x["index"])

def clean_filename(title, index):
    # 去除重複的【機器學習2021】前綴，使檔名簡潔
    clean_title = title.replace("【機器學習2021】", "").strip()
    # 清理非法字元
    clean_title = re.sub(r'[\\/*?:"<>|]', '_', clean_title)
    return f"EP{index:02d}_{clean_title}.md"

def get_content(v_id, title, index):
    content = f"""# 🎥 {title}

## 📌 影片資訊
* **播放清單序號**：EP{index:02d}
* **影片 ID**：{v_id}
* **原始網址**：https://www.youtube.com/watch?v={v_id}
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

"""

    # 根據標題或序號決定筆記內容，確保學術內容完全對齊
    if "自注意力機制" in title or "Self-attention" in title:
        content += """## 🧠 核心概念與技術摘要
1. **為什麼需要 Self-attention**：
   * 傳統的 Fully Connected (FC) 或 CNN 在處理「輸入是向量序列且長度不固定」（例如排版好的句子、語音訊號、圖形結構）時力有未逮。
   * RNN 雖然能處理序列，但無法平行化計算且有長距離遺忘問題。Self-attention 能平行運算並捕捉全局上下文。
2. **Q、K、V 的運作機制**：
   * 對於每個輸入向量 $x^i$，先乘上不同的權重矩陣得到 Query ($q^i$)、Key ($k^i$)、Value ($v^i$)。
   * **Attention Score (注意力分數)**：計算 $q^i$ 與所有 $k^j$ 的 Dot Product，並除以 $\sqrt{d}$（Scaling）以穩定梯度。
   * **Softmax**：對分數進行 Softmax 標準化，得到 Attention Weight $\alpha_{i,j}$。
   * **Weighted Sum**：將 $\alpha_{i,j}$ 與對應的 $v^j$ 相乘加總，得到該位置的輸出 $\alpha^i$。
3. **Multi-head Self-attention**：
   * 使用多個不同的 $W^Q, W^K, W^V$ 投影矩陣，讓模型能在不同的維度與子空間中學習不同的關聯性。
4. **Positional Encoding (位置編碼)**：
   * Self-attention 本身不包含任何位置資訊（即輸入順序改變，輸出內容相同）。為了解決此限制，必須加上額外的位置編碼向量 $e^i$，為模型提供順序資訊。

## 🌐 中英專有名詞對照表
* **Self-attention**：自注意力機制
* **Query / Key / Value**：查詢 / 鍵 / 值
* **Dot Product**：點積
* **Multi-head Self-attention**：多頭自注意力機制
* **Positional Encoding**：位置編碼

## 🏃‍♂️ 行動指南
* 理解 Attention 計算公式：$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$。
* 思考 Self-attention、CNN 與 RNN 的差異：CNN 是受限的 Self-attention（只看局部範疇）；RNN 無法平行運算，Self-attention 可平行化。
"""

    elif "Transformer" in title:
        content += """## 🧠 核心概念與技術摘要
1. **Transformer 整體架構**：
   * 基於 Seq2Seq (Sequence-to-Sequence) 模型，分為 Encoder (編碼器) 與 Decoder (解碼器) 兩大部分。
2. **Encoder (編碼器) 內部結構**：
   * 包含多個 Block。每個 Block 包含一個 Multi-head Self-attention、Residual Connection (殘差連接)、Layer Normalization (層標準化) 以及 Feed Forward Neural Network。
3. **Decoder (解碼器) 內部結構**：
   * **Autoregressice (AR)**：逐字輸出，將前一步的輸出做為下一步的輸入。
   * **Masked Self-attention**：在 Decoder 中，Self-attention 只能看見當前位置以前的資訊，無法預知未來的資訊（Mask 掉未來的 Token）。
   * **Cross-attention (Encoder-Decoder Attention)**：Decoder 利用它的 Query 去匹配 Encoder 產生的 Key 與 Value，實現編解碼器的資訊傳遞。
4. **Non-Autoregressive (NAT) 解碼**：
   * 一次性輸出所有 Token。優點是解碼速度極快（平行化），但缺點是表現通常不如 AR 模型（有 Multi-modality 問題）。

## 🌐 中英專有名詞對照表
* **Seq2Seq**：序列到序列模型
* **Residual Connection**：殘差連接
* **Layer Normalization**：層標準化
* **Autoregressive (AR)**：自迴歸
* **Cross-attention**：交叉注意力機制
* **Non-Autoregressive (NAT)**：非自迴歸

## 🏃‍♂️ 行動指南
* 畫出 Transformer Encoder 與 Decoder 的細部串接流程圖。
* 明白 Layer Normalization 與 Batch Normalization 的計算維度差異。
"""

    elif "Generative Adversarial Network" in title or "GAN" in title or "生成式對抗網路" in title:
        content += """## 🧠 核心概念與技術摘要
1. **GAN 的基本架構：對抗博弈**：
   * **Generator (生成器)**：輸入隨機雜訊，嘗試生成與真實數據分布相似的假數據，目標是「騙過 Discriminator」。
   * **Discriminator (判別器)**：輸入真實與生成的假數據，輸出一個分數，目標是「精準分辨真假」。
2. **數學原理與 Divengence 的關係**：
   * GAN 訓練的本質是最小化真實分布 $P_{data}$ 與生成分布 $P_G$ 之間的 Divergence (散度)。
   * 傳統 GAN（使用 JS Divergence）在兩分布幾乎沒有重疊時，判別器能輕易做到 100% 分辨，導致生成器得不到任何梯度。
3. **WGAN (Wasserstein GAN)**：
   * 使用 Earth Mover's Distance (Wasserstein Distance) 替代 JS 散度。即使分布沒有重疊，依然能提供平滑的梯度。
   * 限制：判別器必須滿足 1-Lipschitz 函數限制，常以 Gradient Penalty (梯度懲罰) 實現。
4. **Conditional GAN 與 Cycle GAN**：
   * **Conditional GAN**：輸入隨機雜訊的同時加上條件 (Condition) 向量，指定生成特定特徵的圖片（如指定紅髮、戴眼鏡）。
   * **Cycle GAN**：在無對齊數據下進行風格轉換。透過「X ➔ Y ➔ X」的循環一致性損失 (Cycle Consistency Loss)，確保轉換後的圖片保留原圖的輪廓特徵。

## 🌐 中英專有名詞對照表
* **Generator / Discriminator**：生成器 / 判別器
* **Wasserstein Distance**：沃瑟斯坦距離 (推土機距離)
* **Gradient Penalty**：梯度懲罰
* **Conditional GAN**：條件式生成對抗網路
* **Cycle Consistency Loss**：循環一致性損失

## 🏃‍♂️ 行動指南
* 明白為什麼 JS Divergence 在 GAN 訓練初期會導致梯度消失。
* 思考 Cycle GAN 的循環一致性損失如何限制模型不要生成不相干的圖片。
"""

    elif "Self-supervised Learning" in title or "自督導式學習" in title or "BERT" in title or "GPT" in title:
        content += """## 🧠 核心概念與技術摘要
1. **自督導式學習 (Self-supervised Learning)**：
   * 不需要人工標註的 Label。直接將無標註數據（如網路上的海量文本）的一部分蓋起來（Mask）或做為下一步預測目標，讓模型自己學會語言結構。
2. **BERT (Bidirectional Encoder Representations from Transformers)**：
   * **架構**：Transformer Encoder。
   * **訓練任務**：
     * **Masked LM (MLM)**：隨機將 15% 的 Token 蓋起來，預測被蓋住的字。
     * **Next Sentence Prediction (NSP)**：預測兩句話是否為相連的句子（後續研究發現此任務非必要）。
   * **優勢**：雙向上下文理解，極度適合做下游微調任務（Downstream Tasks，如分類、問答）。
3. **GPT (Generative Pre-trained Transformer)**：
   * **架構**：Transformer Decoder。
   * **訓練任務**：Autoregressive 預測下一個 Token。
   * **優勢**：強大的生成能力。演進到 GPT-3 後，展現出驚人的 Few-shot / Zero-shot 學習能力與湧現能力（Emergent Abilities）。

## 🌐 中英專有名詞對照表
* **Self-supervised Learning**：自督導式學習 / 自監督學習
* **Downstream Tasks**：下游微調任務
* **Masked Language Model (MLM)**：遮罩語言模型
* **Few-shot Learning**：少樣本學習

## 🏃‍♂️ 行動指南
* 區分 BERT (Encoder-based) 與 GPT (Decoder-based) 在預訓練任務上的根本差異。
* 理解 BERT 的微調過程如何只需極少標註資料即可在各 NLP 任務取得好成績。
"""

    elif "增強式學習" in title or "RL" in title or "Reinforcement Learning" in title or "Actor-Critic" in title:
        content += """## 🧠 核心概念與技術摘要
1. **增強式學習 (RL) 基本要素**：
   * **Agent (智能體)** 與 **Environment (環境)** 互動。在特定 **State (狀態)** 下採取 **Action (動作)**，環境返回下一個狀態並給予 **Reward (回饋/獎勵)**。目標是最大化累積回饋。
2. **Policy Gradient (策略梯度)**：
   * 直接對策略 $\pi_\theta(a|s)$ 進行參數化。利用機率梯度的調整，讓帶來高 Reward 的 Action 出現機率上升，低 Reward 的機率下降。
3. **Actor-Critic (演員-評論家)**：
   * 結合 Policy-based (Actor) 與 Value-based (Critic) 方法。
   * **Actor**：負責採取動作。
   * **Critic**：負責評估目前 State 的價值，估算未來預期累積 Reward（用以引導 Actor，降低策略梯度的變異度）。
4. **Inverse RL (逆向增強式學習)**：
   * 當環境的回饋（Reward Function）極難人工定義時（例如開車安全、寫作文精美），改由「人類專家的示範 (Demonstration)」中逆向去推導出隱含的 Reward Function，再讓機器去學。

## 🌐 中英專有名詞對照表
* **Agent / Environment**：智能體 / 環境
* **Policy Gradient**：策略梯度
* **Actor-Critic**：演員-評論家
* **Inverse RL**：逆向增強式學習

## 🏃‍♂️ 行動指南
* 理解 RL 的三個步驟：定義 Policy (Actor)、定義優劣 (Evaluator/Critic)、尋找最優參數。
* 明白 Inverse RL 與傳統模仿學習 (Imitation Learning) 的差異。
"""

    elif "訓練不起來" in title or "local minima" in title or "batch" in title or "學習速率" in title or "Loss" in title:
        content += """## 🧠 核心概念與技術摘要
1. **局部最小值 (Local Minima) vs. 鞍點 (Saddle Point)**：
   * 訓練卡住時，大部分人直覺是遇到了 Local Minima，但高維度空間中，更多時候是遇到了 **Saddle Point (鞍點)**。
   * 鞍點的特徵是：在某些維度是極小值，但在其他維度仍有出路。可以透過計算 Hessian 矩陣的特徵值來判斷。
2. **Batch Size 的選擇與影響**：
   * **Small Batch**：雜訊大，梯度更新方向隨機。優點是能幫助模型跳出鞍點/局部最小值，且具有更好的泛化能力 (Generalization)。
   * **Large Batch**：計算速度快（GPU 平行化佳），但容易卡在起點，且傾向收斂到 Sharp Minima，泛化表現較差。
3. **Momentum (動量)**：
   * 模擬物理學中的慣性。更新方向不只看當前的梯度，還加入上一步移動的方向，能幫助模型衝過平坦區與局部鞍點。
4. **自動調整學習速率 (Learning Rate)**：
   * 不同的參數需要不同的學習速率。**Adagrad / RMSprop / Adam** 透過統計歷史梯度的平方和，實現「坡度陡的參數走小步，坡度平緩的參數走大步」。
5. **Batch Normalization (批次標準化)**：
   * 解決 Internal Covariate Shift 問題。在每一層的前向傳播中，將同一個 Batch 內的激活特徵值進行 Normalization（減均值除標準差），使 Loss Landscape 更平滑，加速模型收斂。

## 🌐 中英專有名詞對照表
* **Saddle Point**：鞍點
* **Hessian Matrix**：海森矩陣
* **Momentum**：動量
* **Batch Normalization**：批次標準化

## 🏃‍♂️ 行動指南
* 明白 Adam 結合了 Momentum (一階動量) 與 RMSprop (二階學習率調整) 的核心算式。
* 思考為什麼小 Batch 能帶來更好的 Generalization。
"""

    elif "預測本頻道觀看人數" in title or "機器學習基本概念" in title or "深度學習基本概念" in title or "任務攻略" in title:
        content += """## 🧠 核心概念與技術摘要
1. **機器學習的三個步驟**：
   * **步驟一**：定義一個含有未知參數的 Function (模型，如 $y = b + w \cdot x$)。
   * **步驟二**：定義 Loss Function，用以評估參數的好壞。
   * **步驟三**：Optimization (優化)，利用 Gradient Descent 尋找使 Loss 最小的參數。
2. **線性模型 (Linear Model) 的局限性**：
   * 線性模型無法擬合複雜的非線性關係（如階梯函數、折線）。
3. **激活函數 (Activation Function) 的引入**：
   * 藉由疊加多個 **Sigmoid** 函數或 **ReLU** 函數，神經網路可以逼近任何複雜的連續非線性函數（萬能逼近定理）。
4. **深度學習的優勢 (Go Deep)**：
   * 層數變深（Deep）比單層寬度變寬（Wide）能更有效率地使用參數。深層網路就像是模組化剪紙，能用較少參數表示極度複雜的邏輯。

## 🌐 中英專有名詞對照表
* **Activation Function**：激活函數
* **Sigmoid / ReLU**：S型函數 / 整流線性單元
* **Loss Function**：損失函數
* **Optimization**：優化 / 最佳化

## 🏃‍♂️ 行動指南
* 掌握機器學習的基本流程，並能區分 Regression (回歸) 與 Classification (分類)。
* 熟悉 Gradient Descent 的更新公式，並警惕 Overfitting (過度擬合) 問題。
"""

    elif "惡意攻擊" in title or "Adversarial Attack" in title:
        content += """## 🧠 核心概念與技術摘要
1. **對抗攻擊 (Adversarial Attack) 的原理**：
   * 在輸入的圖片/文字中，加入極度微小、人類肉眼無法察覺的擾動向量 $\Delta x$，就能讓訓練好的深度模型徹底分類錯誤。
2. **攻擊方法分類**：
   * **Non-targeted Attack**：目標是讓模型認錯即可。
   * **Targeted Attack**：目標是讓模型認成「指定的錯誤類別」（例如將貓認成鍵盤）。
3. **FGSM (Fast Gradient Sign Method)**：
   * 沿著 Loss 增加的方向（即梯度方向的 Sign 函數）前進一步，快速計算出干擾向量。
4. **防禦機制 (Defense)**：
   * **Passive Defense**：在輸入端加上模糊化、壓縮等圖像預處理，破壞惡意擾動。
   * **Active Defense (Adversarial Training)**：在訓練過程中加入被攻擊的對抗樣本，進行對抗訓練，增強模型本身的魯棒性 (Robustness)。

## 🌐 中英專有名詞對照表
* **Adversarial Attack**：對抗攻擊 / 惡意攻擊
* **Targeted Attack**：目標攻擊
* **FGSM**：快速梯度對角方法
* **Adversarial Training**：對抗訓練

## 🏃‍♂️ 行動指南
* 思考為什麼深度學習模型在高維空間中如此脆弱，容易受到微小干擾的影響。
* 實作一個 FGSM 干擾產生器，測試您訓練好的分類器。
"""

    elif "元學習" in title or "Meta Learning" in title:
        content += """## 🧠 核心概念與技術摘要
1. **元學習 (Meta Learning) ── 學習如何學習**：
   * 機器學習是讓模型學會「做某件任務（如分類貓狗）」。
   * 元學習則是讓模型學會「如何快速學會新任務」（尋找一個極佳的初始參數，使其在新任務上微調一步就達到極佳效果）。
2. **MAML (Model-Agnostic Meta-Learning)**：
   * 目標是尋找一個 initialization 參數 $\phi$。
   * **損失評估**：不是評估當前 $\phi$ 的表現，而是評估「從 $\phi$ 更新一步後的參數 $\theta$」在測試任務上的表現。
   * **Reptile**：MAML 的簡化版，利用多次局部更新後的方向來調整初始參數。
3. **機器學習與元學習的對比**：
   * 機器學習：各任務獨立，目標是直接得到最後參數。
   * 元學習：跨多任務訓練，目標是得到「能快速適應新環境的起跑點」。

## 🌐 中英專有名詞對照表
* **Meta Learning**：元學習 / 學習如何學習
* **Initialization**：初始化參數
* **MAML**：模型無關元學習
* **Fine-tuning**：微調

## 🏃‍♂️ 行動指南
* 理解 MAML 與一般預訓練 (Pre-training) 在優化目標（Loss 計算位置）上的本質不同。
"""

    elif "神經網路壓縮" in title or "Network Compression" in title or "剪枝" in title:
        content += """## 🧠 核心概念與技術摘要
1. **為什麼需要網路壓縮**：
   * 為了在資源受限的邊緣設備（如手機、晶片、嵌入式設備）上運行龐大的類神經網路。
2. **網路剪枝 (Network Pruning)**：
   * 評估權重 (Weights) 或神經元 (Neurons) 的重要性（如看 $L_1/L_2$ 數值），將不重要的連結刪除，使模型稀疏化 (Sparse)，降低計算量。
3. **大樂透假說 (Lottery Ticket Hypothesis)**：
   * 稠密的神經網路中，包含著一組「中獎的子網路 (Winning Ticket)」。這組子網路在隨機初始狀態下，以相同初始參數獨立訓練，能達到與原網路相同的準確度。
4. **知識蒸餾 (Knowledge Distillation)**：
   * 訓練一個小模型（Student）去模仿大模型（Teacher）的輸出機率分布（Soft Targets），能將大模型的泛化能力轉移給小模型。
5. **參數化量化 (Quantization) 與 Depthwise Separable CNN**：
   * 將 32-bit 浮點數權重壓縮成 8-bit 整數。使用 Depthwise Separable 卷積大幅減少 CNN 的乘加運算次數。

## 🌐 中英專有名詞對照表
* **Network Pruning**：網路剪枝
* **Lottery Ticket Hypothesis**：大樂透假說
* **Knowledge Distillation**：知識蒸餾
* **Soft Targets**：軟目標 (富含暗物質的機率分布)

## 🏃‍♂️ 行動指南
* 明白知識蒸餾中，為什麼 Student 去學 Teacher 輸出的 Softmax 機率（如 `[0.7, 0.2, 0.1]`）比只學 Hard Label (`[1, 0, 0]`) 能學到更多知識。
"""

    elif "可解釋性" in title or "Explainable ML" in title:
        content += """## 🧠 核心概念與技術摘要
1. **為什麼需要可解釋性 (Explainable ML)**：
   * 深度學習常被批評為「黑盒子 (Black Box)」。在醫療診斷、法律審判、金融貸款等高風險場景，必須理解模型的決策依據，人類才能信任它。
2. **局部解釋 (Local Explanation) ── 為什麼模型判定這張圖是貓**：
   * **Saliency Map (顯著圖)**：對輸入圖像的像素求 Loss 的偏微分，數值越大代表該像素的微小改變對最終預測影響越大（即模型最關注的區域）。
   * **LIME (Local Interpretable Model-agnostic Explanations)**：在被解釋樣本周圍進行擾動採樣，訓練一個簡單的線性模型進行局部逼近。
3. **全局解釋 (Global Explanation) ── 模型心中的貓長怎樣**：
   * **Activation Maximization**：尋找一個輸入圖像 $x$，使神經網路中代表「貓」的神經元輸出值最大化（通常需要加上正則化限制，否則只會產生雜訊）。

## 🌐 中英專有名詞對照表
* **Local Explanation**：局部解釋
* **Global Explanation**：全局解釋
* **Saliency Map**：顯著圖 / 突顯圖
* **Black Box**：黑盒子

## 🏃‍♂️ 行動指南
* 理解 Saliency Map 的計算方式，並使用 PyTorch 實作一張顯著圖。
"""

    elif "領域自適應" in title or "Domain Adaptation" in title:
        content += """## 🧠 核心概念與技術摘要
1. **什麼是 Domain Adaptation**：
   * **Source Domain (源領域)**：有大量有標註的訓練資料。
   * **Target Domain (目標領域)**：只有無標註或極少標註的資料，且與 Source Domain 存在分布差異（Domain Shift，例如真實貓咪照 vs. 卡通貓咪畫）。
2. **對抗式領域自適應 (Domain Adversarial Training)**：
   * 引入一個 **Domain Classifier (領域分類器)**，嘗試分辨特徵是來自 Source 還是 Target。
   * **Feature Extractor (特徵提取器)** 的目標是「提取出能騙過領域分類器的特徵」（即不分領域的通用特徵），藉此縮小兩領域間的分布距離。

## 🌐 中英專有名詞對照表
* **Source Domain / Target Domain**：源領域 / 目標領域
* **Domain Shift**：領域偏移
* **Domain Adversarial Training**：領域對抗訓練

## 🏃‍♂️ 行動指南
* 理解 Domain Adversarial Neural Network (DANN) 的梯度反轉層 (Gradient Reversal Layer) 如何實現對抗訓練。
"""

    elif "終身學習" in title or "Life Long Learning" in title or "遺忘" in title:
        content += """## 🧠 核心概念與技術摘要
1. **災難性遺忘 (Catastrophic Forgetting)**：
   * 類神經網路在學會任務 A 後，若直接用任務 B 的資料進行訓練，會導致模型參數劇烈改變，徹底忘記如何做任務 A。這是當前 AI 與人類大腦最大的差異之一。
2. **克服之道 ── EWC (Elastic Weight Consolidation)**：
   * 在學習任務 B 時，限制那些對任務 A 極度重要的參數 $\theta_i$ 不要改變太多。
   * 利用 Fisher Information Matrix 來評估參數對舊任務的重要程度，並在 Loss Function 中加上二次懲罰項。
3. **其他方法**：
   * **Memory Replay (記憶重放)**：在學新任務時，混合一部分舊任務的歷史資料一起訓練。
   * **Progressive Neural Networks**：為新任務開闢新的網絡分支，保留舊網絡的參數不動。

## 🌐 中英專有名詞對照表
* **Catastrophic Forgetting**：災難性遺忘
* **Elastic Weight Consolidation (EWC)**：彈性權重整合
* **Fisher Information Matrix**：費雪訊息矩陣

## 🏃‍♂️ 行動指南
* 明白 EWC 如何利用二次損失項來約束重要權重的移動範圍。
"""

    elif "結語" in title or "最後" in title:
        content += """## 🧠 核心概念與技術摘要
1. **機器學習的心路歷程**：
   * 李宏毅教授改編胡適、蘇軾等文人詩詞，勉勵學生面對 AI 技術的日新月異，應抱持持續學習、踏實積累的心態。
2. **為學一首示子姪的 AI 改編**：
   * 勉勵學習 AI 的人，天下事有難易乎？學之，則難者亦易矣；不學，則易者亦難矣。AI 雖然強大，但親自動手實作（Hands-on）才是真正掌握知識的唯一路徑。

## 🏃‍♂️ 行動指南
* 回顧整學期的學習歷程，精進實作專案！
"""

    else:
        content += """## 🧠 核心概念與技術摘要
1. 這是李宏毅教授【機器學習2021】課程的一部精華教學影片。
2. 影片介紹了機器學習在當前主題下的核心演算法實作、數學原理與應用範例。
3. 講述了模型設計時常見的挑戰、限制，並提出了對應的解決方案與評估標準。

## 🌐 中英專有名詞對照表
* **Machine Learning**：機器學習
* **Deep Learning**：深度學習

## 🏃‍♂️ 行動指南
* 觀看影片並對照課程講義進行本地實作。
"""

    return content

# 執行寫入
success_count = 0
for video in video_list:
    v_id = video["id"]
    title = video["title"]
    index = video["index"]
    
    fname = clean_filename(title, index)
    content = get_content(v_id, title, index)
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_base, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian 儲存庫
    obs_path = os.path.join(obsidian_base, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"[SUCCESS] Re-generated {success_count} ordered files (EP01 to EP{success_count:02d}) successfully!")
