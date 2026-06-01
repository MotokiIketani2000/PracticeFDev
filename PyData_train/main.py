from pathlib import Path
import argparse
import pandas as pd
from src.extract import extract_data
from src.transform import transform_data


def run_pipeline(src_path: Path, tamed_path: Path, transformed_path: Path):
    tamed_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"抽出: {src_path}")
    df = extract_data(src_path)
    df.to_csv(tamed_path, index=False, encoding="utf-8-sig")
    print(f"抽出データを保存しました: {tamed_path}")

    print("変換を実行します")
    df_trans = transform_data(df)
    df_trans.to_csv(transformed_path, index=False, encoding="utf-8-sig")
    print(f"変換済データを保存しました: {transformed_path}")


def main():
    parser = argparse.ArgumentParser(description="簡易ETLパイプライン（入門用）")
    parser.add_argument("--src", default="./data/raw/data.csv", help="入力CSVパス")
    parser.add_argument("--tamed", default="./data/tamed/tamed_1.csv", help="抽出後の保存先")
    parser.add_argument("--out", default="./data/tamed/transformed.csv", help="変換後の保存先")
    parser.add_argument("--step", choices=["all", "extract", "transform"], default="all", help="実行ステップ")
    args = parser.parse_args()

    src_path = Path(args.src)
    tamed_path = Path(args.tamed)
    out_path = Path(args.out)

    if args.step == "extract":
        df = extract_data(src_path)
        tamed_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(tamed_path, index=False, encoding="utf-8-sig")
        print(f"抽出のみ完了: {tamed_path}")
    elif args.step == "transform":
        df = pd.read_csv(tamed_path)
        df_trans = transform_data(df)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        df_trans.to_csv(out_path, index=False, encoding="utf-8-sig")
        print(f"変換のみ完了: {out_path}")
    else:
        run_pipeline(src_path, tamed_path, out_path)


if __name__ == "__main__":
    main()