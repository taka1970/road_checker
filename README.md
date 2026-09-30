# Road Checker

道路設計の基本項目（勾配・幅員・曲線半径・土量）を自動判定する Python ツールです。  
Excel を読み込み、各項目が基準を満たしているかをチェックし、結果を `result.xlsx` に出力します。

---

## 🚀 Features（機能）

- **勾配チェック（Slope）**
- **幅員チェック（Width）**
- **曲線半径チェック（Curve）**
- **土量チェック（Volume）**
- Excel の自動読み込み（utils/excel_loader.py）
- 判定ロジックのモジュール化（checker/）
- 結果を Excel に自動出力

---

## 📂 Project Structure（構成）
Excel入力（sample_data.xlsx）
          │
          ▼
  ┌────────────────────┐
  │   volume.py（土量判定） │
  └────────────────────┘
          │
          ▼
  土量の計算（盛土・切土）
          │
          ▼
  許容範囲との比較
          │
          ▼
  判定結果（OK / NG）
          │
          ▼
result.xlsx に出力

