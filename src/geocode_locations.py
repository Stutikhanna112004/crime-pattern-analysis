import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def add_coordinates(df, location_column='City'):
    geolocator = Nominatim(user_agent="up-crime-mapper", timeout=10)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=3)

    latitudes = []
    longitudes = []

    for city in df[location_column]:
        try:
            location = geocode(str(city) + ", Uttar Pradesh, India")
            if location:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
            else:
                latitudes.append(None)
                longitudes.append(None)
        except Exception as e:
            print(f"❌ Geocoding error for {city}: {e}")
            latitudes.append(None)
            longitudes.append(None)

    df['Latitude'] = latitudes
    df['Longitude'] = longitudes
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/UP_Crime_2019_clean.csv")
    df.columns = df.columns.str.strip() 

    if 'City' not in df.columns:
        raise Exception("⚠️ 'City' column not found. Please check your dataset.")

    df_geo = add_coordinates(df, location_column='City')
    df_geo.to_csv("data/cleaned/UP_Crime_with_coordinates.csv", index=False)
    print("✅ Geocoded dataset saved to: data/cleaned/UP_Crime_with_coordinates.csv")
