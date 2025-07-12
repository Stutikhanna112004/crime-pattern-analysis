import pandas as pd
import glob

def load_all_years(data_path="data/raw/"):
    files = glob.glob(data_path + "*.csv")
    df_list = []
    
    for f in files:
        df_temp = pd.read_csv(f)
        if 'Date' in df_temp.columns:
            df_temp['Date'] = pd.to_datetime(df_temp['Date'], errors='coerce')
        else:
            print(f"⚠️ Warning: 'Date' column missing in {f}")
        df_list.append(df_temp)
    
    return pd.concat(df_list, ignore_index=True)

if __name__ == "__main__":
    df = load_all_years()
    print("✅ Loaded data shape:", df.shape)
    df.to_csv("data/cleaned/all_years_combined.csv", index=False)
    print("📝 Saved combined data to: data/cleaned/all_years_combined.csv")
