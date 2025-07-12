from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np  # ✅ Import numpy

def identify_hotspots(df, eps=0.01, min_samples=5):
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

    if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
        raise ValueError("🛑 'Latitude' or 'Longitude' columns not found in dataset.")

    coords = df[['Latitude', 'Longitude']].dropna()
    db = DBSCAN(eps=eps, min_samples=min_samples, metric='haversine').fit(np.radians(coords))
    coords['Cluster'] = db.labels_
    df = df.merge(coords, how='left', on=['Latitude', 'Longitude'])
    return df


if __name__ == "__main__":
    import pandas as pd

    # Load your cleaned dataset
    df = pd.read_csv("data/cleaned/UP_Crime_with_coordinates.csv")

    # Run clustering
    clustered_df = identify_hotspots(df)

    # Save result to output folder
    clustered_df.to_csv("data/output/UP_Crime_with_clusters.csv", index=False)

    # Show a summary
    print("✅ Clustering complete.")
    print("Number of clusters (excluding noise):", clustered_df['Cluster'].nunique() - (1 if -1 in clustered_df['Cluster'].unique() else 0))
    print(clustered_df['Cluster'].value_counts().head())
