import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    required_col = ["年月日","平均気温(℃)"]
    df = df[required_col].copy()
    df["date"] = pd.to_datetime(df["年月日"],errors="coerce")
    df["temp_avg"] = pd.to_number(df["平均気温(℃)"].astype(float),errors="coerce")
    df = df.dropna(subset=["date","temp_avg"])
    
    print("変換後のデータの最初の3行は")
    print(df.head(3))
    return df


    