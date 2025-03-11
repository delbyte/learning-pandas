import pandas as pd
import numpy as np 
import geopandas as gpd
import geodatasets 
from geodatasets import get_path

path_to_data = get_path("absaustralia_states_territories")
gdf = gpd.read_file(path_to_data)