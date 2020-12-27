import folium
import pandas as pd 
import folium.plugins as plugins
from folium.plugins import MarkerCluster


df = pd.read_csv('IPs_INFO.csv')

locs = df[["Latitude", "Longitude"]].values.tolist()
pops = df[["IP", "Location", "Latitude", "Longitude"]].values.tolist()


m = folium.Map([42.363,-71.0995],zoom_start=3)


MarkerCluster(locations=locs, popups=pops).add_to(m)

m.save("MAP_output.html")
