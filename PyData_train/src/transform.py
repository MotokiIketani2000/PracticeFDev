import pandas as pd
from typing import Optional


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """シンプルで分かりやすい変換処理（入門向け）。

    - 日本語ヘッダの `年月日` と `平均気温(℃)` を受け取り、
      `date`（datetime）と`temp_avg`（float）を持つデータフレームを返します。
    - 欠損や不正な行を除去し、日付でソートします。

    Args:
        df: 抽出された元データのDataFrame

    Returns:
        変換済みDataFrame（`date`, `temp_avg` を含む）
    """
    # まず必要なカラムがあるか安全に取り出す
    required = [col for col in ["年月日", "平均気温(℃)"] if col in df.columns]
    if len(required) < 2:
        raise ValueError("入力データに必要なカラムがありません: 年月日, 平均気温(℃)")

    work = df[required].copy()
    work = work.rename(columns={"年月日": "年月日", "平均気温(℃)": "平均気温(℃)"})

    # 型変換（エラーは欠損として扱う）
    work["date"] = pd.to_datetime(work["年月日"], errors="coerce")
    work["temp_avg"] = pd.to_numeric(work["平均気温(℃)"], errors="coerce")

    # 欠損値のある行を除外
    work = work.dropna(subset=["date", "temp_avg"]).reset_index(drop=True)

    # 日付でソートして重複を削除
    work = work.sort_values("date").drop_duplicates(subset=["date"]).reset_index(drop=True)

    # 最終的に必要な列だけ残す
    result = work[["date", "temp_avg"]].copy()

    print("transform: 最初の3行")
    print(result.head(3))
    return result


__all__ = ["transform_data"]
