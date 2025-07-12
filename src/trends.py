import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_yearly_trends(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Year', hue='Season')
    plt.title("Crime Trends by Year and Season")
    plt.savefig("data/output/trends_by_season.png")
    print("📊 Saved plot: data/output/trends_by_season.png")

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/UP_Crime_2019_clean.csv")
    plot_yearly_trends(df)
    print("✅ Yearly trend plot complete.")

