import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample DataFrame with predicted coordinates (replace with your actual data)
data = {
    'latitude': [45.4642, 45.4655, 45.4667],
    'longitude': [9.1900, 9.1915, 9.1930]
}
df = pd.DataFrame(data)

# Function to create a Folium map with markers
def create_map(df):
    # Create a Folium map centered around the mean of the coordinates
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)

    # Add markers for each predicted fire coordinate
    for _, row in df.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']], popup=f"Lat: {row['latitude']}, Lon: {row['longitude']}").add_to(m)

    return m

# Main Streamlit app code
def main():
    st.title('Predicted Fire Locations in Italy')
    st.write('Below is a map showing the predicted fire locations:')
    
    # Display the map using Streamlit-Folium
    folium_map = create_map(df)
    st_folium(folium_map)

if __name__ == '__main__':
    main()
