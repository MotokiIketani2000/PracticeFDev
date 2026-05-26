from pathlib import Path
from src.extract import extract_data
from src.transfform import transform_data

if __name__ == "__main__":
    filepath = Path("./data/raw/data.csv")
    df = extract_data(filepath)
    df = transform_data(df)
    print("データの最初の3行は")
    print(df.head(3))