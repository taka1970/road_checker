import pandas as pd
from utils.excel_loader import load_excel
from utils.validator import is_valid_row
from checker.slope import check_slope
from checker.width import check_width
from checker.curve import check_curve
from checker.volume import check_volume

def main():
    df = load_excel("sample/sample_data.xlsx")
    if df is None:
        print("データ読み込み失敗")
        return

    results = []

    for index, row in df.iterrows():
        if not is_valid_row(row):
            results.append(["NG（空欄あり）"])
            continue

        start_elev = row["起点標高"]
        end_elev = row["終点標高"]
        length = row["延長(m)"]
        road_width = row["車道幅員(m)"]
        radius = row["曲線半径R(m)"]
        cut = row["切土量(m3)"]
        fill = row["盛土量(m3)"]

        slope_value, slope_ok = check_slope(start_elev, end_elev, length)
        width_ok = check_width(road_width)
        curve_ok = check_curve(radius)
        volume_ok = check_volume(cut, fill)

        results.append([
            slope_value,
            "OK" if slope_ok else "NG",
            "OK" if width_ok else "NG",
            "OK" if curve_ok else "NG",
            "OK" if volume_ok else "NG"
        ])

    result_df = pd.DataFrame(results, columns=[
        "勾配(%)", "勾配判定", "幅員判定", "曲線半径判定", "土量判定"
    ])

    # CSV 出力
    result_df.to_csv("result.csv", index=False)

    # Excel 出力（文字化けしない）
    result_df.to_excel("result.xlsx", index=False)

    print("result.csv と result.xlsx を出力しました")

if __name__ == "__main__":
    main()
