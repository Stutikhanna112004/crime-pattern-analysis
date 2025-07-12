import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import folium_static
import plotly.express as px

# Load and preprocess
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned/UP_Crime_with_coordinates.csv")
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Latitude', 'Longitude'])
    df.fillna('', inplace=True)
    return df

# Calculate severity level (1 to 5)
def calculate_severity(row):
    score = 0
    try:
        score += int(row.get('Number of child victims', 0))
        score += int(row.get('Number of male(adult)', 0))
        score += int(row.get('Number of female(adult)', 0))
    except:
        pass
    return min(5, max(1, score // 2))  # Normalize to 1–5

# Color based on severity
def severity_color(severity):
    return {
        1: "green",
        2: "lightgreen",
        3: "orange",
        4: "red",
        5: "darkred"
    }.get(severity, "gray")

# Generate map
def generate_map(df):
    m = folium.Map(location=[26.85, 80.95], zoom_start=6)

    # HeatMap Layer
    heat_data = df[['Latitude', 'Longitude']].values.tolist()
    HeatMap(heat_data, radius=10, blur=15).add_to(m)

    # Marker Cluster
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        severity = calculate_severity(row)
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5 + severity,
            color=severity_color(severity),
            fill=True,
            fill_opacity=0.7,
            popup=folium.Popup(f"""
                <b>City:</b> {row.get('City', 'N/A')}<br>
                <b>Title:</b> {row.get('Title', 'N/A')}<br>
                <b>Text:</b> {row.get('Text', '')}<br>
                <b>Child victims:</b> {row.get('Number of child victims', 0)}<br>
                <b>Adults:</b> 👨 {row.get('Number of male(adult)', 0)} 👩 {row.get('Number of female(adult)', 0)}<br>
            """, max_width=250)
        ).add_to(marker_cluster)

    return m
import plotly.express as px

def show_top_crime_types(df, title_col='Title'):
    st.subheader("📊 Top Reported Crime Types")
    top_crimes = df[title_col].value_counts().nlargest(10)
    fig = px.bar(top_crimes, x=top_crimes.index, y=top_crimes.values,
                 labels={'x': 'Crime Type', 'y': 'Number of Cases'},
                 color=top_crimes.values,
                 color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)

def show_monthly_trend(df, date_col='Date'):
    if date_col not in df.columns:
        st.warning("📅 No 'Date' column available to plot time trends.")
        return

    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df['Month'] = df[date_col].dt.to_period("M")
    trend = df.groupby('Month').size().reset_index(name='Crimes')
    trend['Month'] = trend['Month'].astype(str)

    fig = px.line(trend, x='Month', y='Crimes', markers=True, title="📈 Monthly Crime Trend")
    st.plotly_chart(fig, use_container_width=True)

def show_victim_pie(df):
    st.subheader("👥 Victim Demographics (Optional)")
    labels = ['Child Victims', 'Male Adults', 'Female Adults']
    values = [
        df['Number of child victims'].astype(int).sum(),
        df['Number of male(adult)'].astype(int).sum(),
        df['Number of female(adult)'].astype(int).sum()
    ]
    fig = px.pie(values=values, names=labels, title="Victim Distribution")
    st.plotly_chart(fig)


# Streamlit App UI
st.set_page_config(page_title="UP Crime Dashboard", layout="wide")
st.title("🔍 UP Crime Pattern Analysis Dashboard")
st.markdown("This dashboard visualizes crime hotspots in Uttar Pradesh using clustering and victim data.")

# Load Data
df = load_data()

# City Filter
cities = sorted(df['City'].dropna().unique())
selected_city = st.selectbox("📍 Filter by City", options=["All"] + cities)

if selected_city != "All":
    df = df[df['City'] == selected_city]

# Generate and show map
map_ = generate_map(df)
folium_static(map_)
st.markdown("---")
st.header("📊 Crime Pattern Analysis") 
def show_victim_pie(df):
    st.subheader("👥 Victim Demographics")

    # Use to_numeric with errors='coerce' to handle non-numeric values like ''
    child_victims = pd.to_numeric(df['Number of child victims'], errors='coerce').fillna(0).sum()
    male_adults = pd.to_numeric(df['Number of male(adult)'], errors='coerce').fillna(0).sum()
    female_adults = pd.to_numeric(df['Number of female(adult)'], errors='coerce').fillna(0).sum()

    labels = ['Child Victims', 'Male Adults', 'Female Adults']
    values = [child_victims, male_adults, female_adults]

    fig = px.pie(values=values, names=labels, title="Victim Distribution")
    st.plotly_chart(fig)


show_top_crime_types(df)

if {'Number of child victims', 'Number of male(adult)', 'Number of female(adult)'}.issubset(df.columns):
    show_victim_pie(df)


