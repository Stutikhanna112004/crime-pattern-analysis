# crime-pattern-analysis
🔍 Crime Pattern Analysis in Uttar Pradesh (India) Identify crime hotspots, visualize trends, and recommend police deployment using geospatial clustering and FIR data. Built with Python, Folium, and Streamlit.

---

## 🚀 Features

✅ Interactive **folium heatmaps**  
✅ Marker clustering with detailed crime info  
✅ Severity-based hotspot highlighting (by victim count)  
✅ Streamlit dashboard with **city filtering**  
✅ 📊 Data visualizations (top crime types, time trends, demographics)  
✅ Modular, clean code structure for easy scaling

---

## 🗃️ Project Structure

up-crime/
│
├── data/
│ ├── raw/ 
│ ├── cleaned/ 
│ │ ├── all_years_combined.csv
│ │ ├── UP_Crime_2019_clean.csv
│ │ └── UP_Crime_with_coordinates.csv
│ └── output/ 
│ ├── crime_heatmap.html
│ ├── UP_Crime_with_clusters.csv
│ └── deployment_recommendations.csv
│
├── src/ 
│ ├── clean_data.py 
│ ├── clustering.py 
│ ├── geocode_locations.py 
│ ├── load_data.py 
│ ├── trends.py 
│ ├── visualize.py 
│ └── allocation.py 
│
├── app.py 
├── requirements.txt 
└── README.md 

### 🔥 Hotspot Heatmap with Marker Clusters
- City-level filtering
- Clickable markers with detailed info
- Severity-based circle coloring

### 📊 Trend & Type Analysis
- Top reported crimes
- Line chart of monthly crime counts
- Victim demographics (children, male, female)

---
1. Set up a virtual environment
python -m venv .venv
source .venv/bin/activate
   
2. Install dependencies
pip install -r requirements.txt

3. Launch the dashboard
streamlit run app.py

📈 Technologies Used
Python - pandas, numpy, geopandas
Geospatial Tools - folium, geopy, plotly
ML Algorithm - DBSCAN for density-based clustering
Dashboard - Streamlit
Mapping - Leaflet.js via folium

Data Source
-FIR datasets sourced from Kaggle

About Me-
👩‍💻 Stuti Khanna
Data Analyst | Explorer | Third Year Student

⚠️ Copyright Notice
This project is licensed for educational and non-commercial use only.

🛡️ Copyright © 2025 Stuti Khanna
Do not reuse logic, visuals, or deployment flows without permission.
For collaboration or citations, contact me on LinkedIn.
https://in.linkedin.com/in/stuti-khanna-3612b92a0?trk=people-guest_people_search-card

⭐ Show Some Love
If this project helped or inspired you, please consider giving it a ⭐ on GitHub. It really helps! 💖
