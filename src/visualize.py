import pandas as pd
import folium
from folium.plugins import HeatMap

def create_heatmap(df, filename="data/output/crime_heatmap.html"):
    m = folium.Map(location=[26.85, 80.95], zoom_start=7)
    heat_df = df[['Latitude', 'Longitude']].dropna()
    HeatMap(heat_df.values, radius=8).add_to(m)
    m.save(filename)
    print(f"🗺️  Heatmap saved to {filename}")

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/UP_Crime_with_coordinates.csv")
    create_heatmap(df)
    print("✅ Heatmap created.")
