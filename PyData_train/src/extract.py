import re
import pandas as pd
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "data.csv"


def _find_first_date_row(df: pd.DataFrame) -> Optional[int]:
    date_re = re.compile(r"^\d{4}/\d{1,2}/\d{1,2}")
    for idx, val in enumerate(df.iloc[:, 0].astype(str)):
        if pd.isna(val):
            continue
        if date_re.match(val.strip()):
            return idx
    return None


def extract_data(file_path: Path) -> pd.DataFrame:
    # Read file as text to detect header and then parse CSV from that point
    from io import StringIO

    with open(file_path, encoding="cp932", errors="replace") as f:
        lines = f.readlines()

    # build a temporary dataframe of first column values to detect date row
    first_col_vals = [line.split(",")[0] if line.strip() != "" else "" for line in lines]

    # find index of first date-like row
    first_date_idx = None
    date_re = re.compile(r"^\d{4}/\d{1,2}/\d{1,2}")
    for idx, val in enumerate(first_col_vals):
        if val and date_re.match(val.strip()):
            first_date_idx = idx
            break

    if first_date_idx is None:
        header_idx = 0
        start_idx = 0
    else:
        header_idx = None
        for j in range(max(0, first_date_idx - 4), first_date_idx):
            if any(x.strip() for x in lines[j].split(",")):
                header_idx = j
                break
        if header_idx is None:
            header_idx = max(0, first_date_idx - 1)
        start_idx = header_idx

    csv_text = "".join(lines[start_idx:])
    # read without inferring header so we can promote the correct row
    tmp = pd.read_csv(StringIO(csv_text), header=None)

    # try to locate a row that contains the Japanese header '年月日' and promote it
    header_row = None
    for idx, row in tmp.iterrows():
        if row.astype(str).str.contains("年月日").any():
            header_row = idx
            break

    if header_row is not None:
        tmp.columns = tmp.iloc[header_row].fillna("").astype(str).str.strip()
        df = tmp.iloc[header_row + 1 :].reset_index(drop=True)
    else:
        # fallback: use pandas header inference
        df = pd.read_csv(StringIO(csv_text))

    # keep only rows where the first column looks like a date (YYYY/M/D)
    date_re = re.compile(r"^\d{4}/\d{1,2}/\d{1,2}")
    first_col = df.iloc[:, 0].astype(str)
    mask = first_col.str.match(date_re)
    if mask.any():
        df = df[mask].reset_index(drop=True)
    else:
        # fallback: use pandas header inference
        df = pd.read_csv(StringIO(csv_text))

    # keep only the actual measurement columns: date, average, max, min
    if df.shape[1] >= 8:
        df = df.iloc[:, [0, 1, 4, 7]].copy()
        df.columns = ["年月日", "平均気温(℃)", "最高気温(℃)", "最低気温(℃)"]

    # drop fully empty columns, then keep a stable column order
    df = df.dropna(axis=1, how="all")
    df = df[[col for col in ["年月日", "平均気温(℃)", "最高気温(℃)", "最低気温(℃)"] if col in df.columns]]

    print("抽出後のカラム:")
    print(list(df.columns)[:20])
    return df


if __name__ == "__main__":
    df = extract_data(DEFAULT_DATA_PATH)
    print(df.head(3))
