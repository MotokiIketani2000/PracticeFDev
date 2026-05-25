# pydata-train

気象データの読み込み・分析用プロジェクト（uv + Python 3.14）。

## ディレクトリ構成

```
PyData_train/
├── .venv/              # 仮想環境（uv が作成）
├── data/
│   ├── raw/            # 生データ（CSV など）
│   └── weather.db
├── src/
│   └── extract.py      # CSV 読み込み
├── main.py
├── pyproject.toml
└── uv.lock
```

## 実行方法

**必ず `PyData_train` ディレクトリで** 次のいずれかを使う。

```bash
# 推奨: 仮想環境を自動で使う
uv run python src/extract.py

# または venv を有効化してから
source .venv/bin/activate
python src/extract.py
```

macOS ではシステムに `python` コマンドが無いことが多い。`python3` や上記の `uv run` / 有効化後の `python` を使う。

## 依存関係の追加

```bash
uv add パッケージ名
```
