import pandas as pd

def preprocess(df, skip_date=False):
    if not skip_date and 'Date' in df.columns:
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['Hour'] = df['Date'].dt.hour
        df['DayOfWeek'] = df['Date'].dt.day_name()

        season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                      3: 'Spring', 4: 'Spring', 5: 'Summer',
                      6: 'Monsoon', 7: 'Monsoon', 8: 'Monsoon',
                      9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
        df['Season'] = df['Month'].map(season_map)
        df['TimeOfDay'] = df['Hour'].apply(lambda x: 'Night' if x >= 20 or x <= 4 else 'Day')
    else:
        print("⚠️ 'Date' column missing — skipping temporal feature extraction.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/all_years_combined.csv")
    df_clean = preprocess(df, skip_date=True)
    df_clean.to_csv("data/cleaned/UP_Crime_2019_clean.csv", index=False)
    print("✅ Cleaned data saved to: data/cleaned/UP_Crime_2019_clean.csv")
