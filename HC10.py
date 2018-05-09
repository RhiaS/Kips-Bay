import folium
import pandas as pd

complaints = pd.read_csv('numbers2.csv')
complaints = complaints.fillna(0)
print(complaints["Complaint Type"])

mapCompl = folium.Map(location=[40.75, -74.125], zoom_start=15, tiles='CartoDB')

for index,row in complaints.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    if not lat == 0:
        name = row["Complaint Type"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapCompl)
        
mapCompl.save(outfile='311map.html')
