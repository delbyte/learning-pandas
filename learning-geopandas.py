import pandas as pd
import numpy as np 
import geopandas as gpd
import geodatasets 
from geodatasets import get_path
import matplotlib.pyplot as plt
from shapely.geometry import Point

path_to_data = get_path("absaustralia_states_territories")
gdf = gpd.read_file(path_to_data)

gdf = gdf.rename(columns={c: str(c) for c in gdf.columns})

print(gdf.info())
print("\n\n")
print(gdf)
m = gdf.explore()

outfp = r"base_map.html"
m.save(outfp)
import webbrowser
webbrowser.open(outfp)