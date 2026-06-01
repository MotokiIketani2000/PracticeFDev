# pydata-train

入門向けの簡易ETLパイプライン例です。生データ（CSV）を読み取り、簡単な前処理を行って保存します。

構成の要点
- 生データ: `data/raw/data.csv`
- 抽出後（そのまま保存）: `data/tamed/tamed_1.csv`
- 変換後（時系列＋平均気温）: `data/tamed/transformed.csv`

実行方法（簡単）

1. 仮想環境を作る / 有効化（推奨）

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # または pyproject の依存をインストール
```

2. パイプライン実行（プロジェクトルートで）

```bash
python main.py           # 抽出→変換 を実行して結果を保存します
# 個別実行例:
python main.py --step extract   # 抽出のみ
python main.py --step transform # 変換のみ（事前に tamed の CSV が必要）
```

学習のポイント
- `src/extract.py` : 生データから必要な行・列を抽出する処理（文字コードやヘッダのばらつきを扱う）
- `src/transform.py`: 日付や数値の変換、欠損除去、ソートなど基本的な前処理
- `main.py`: パイプラインの実行とファイルの入出力を担当。初心者が ETL の流れを追いやすい構成にしています。

問題があれば `data/raw/data.csv` のサンプルと一緒に相談してください。
