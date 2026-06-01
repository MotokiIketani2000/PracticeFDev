from pathlib import Path
from src.extract import extract_data
from src.transfform import transform_data

if __name__ == "__main__":
    filepath = Path("./data/raw/data.csv")
    output_path = Path("./data/tamed/tamed_1.csv")

    df = extract_data(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    df = transform_data(df)
    print("データの最初の3行は")
    print(df.head(3))
    print(f"保存しました: {output_path}")