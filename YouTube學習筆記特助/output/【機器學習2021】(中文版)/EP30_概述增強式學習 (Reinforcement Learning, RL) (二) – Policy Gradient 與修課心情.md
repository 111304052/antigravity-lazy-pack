# 🎥 【機器學習2021】概述增強式學習 (Reinforcement Learning, RL) (二) – Policy Gradient 與修課心情

## 📌 影片資訊
* **播放清單序號**：EP30
* **影片 ID**：US8DFaAZcp4
* **原始網址**：https://www.youtube.com/watch?v=US8DFaAZcp4
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **增強式學習 (RL) 基本要素**：
   * **Agent (智能體)** 與 **Environment (環境)** 互動。在特定 **State (狀態)** 下採取 **Action (動作)**，環境返回下一個狀態並給予 **Reward (回饋/獎勵)**。目標是最大化累積回饋。
2. **Policy Gradient (策略梯度)**：
   * 直接對策略 $\pi_	heta(a|s)$ 進行參數化。利用機率梯度的調整，讓帶來高 Reward 的 Action 出現機率上升，低 Reward 的機率下降。
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
