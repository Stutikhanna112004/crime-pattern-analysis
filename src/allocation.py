import pandas as pd

def recommend_deployment(df):
    cluster_counts = df.groupby(['Cluster']).size().reset_index(name='CrimeCount')
    top_clusters = cluster_counts.sort_values('CrimeCount', ascending=False).head(10)
    top_clusters.to_csv("data/output/deployment_recommendation.csv", index=False)
    return top_clusters

if __name__ == "__main__":
    df = pd.read_csv("data/output/UP_Crime_with_clusters.csv")
    result = recommend_deployment(df)
    print("✅ Top deployment zones:")
    print(result)
    print("📝 Saved to: data/output/deployment_recommendation.csv")
