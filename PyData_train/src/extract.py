import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "data.csv"


def extract_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path, encoding="shift_jis")
    print("データの最初の３行は")
    print(df.head(3))
    return df


if __name__ == "__main__":
    df = extract_data(DEFAULT_DATA_PATH)
