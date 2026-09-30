import pandas as pd

def load_excel(path: str):
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        print(f"Excel読み込みエラー: {e}")
        return None
