# Import modules

import helpers as h
import pandas as pd
import json
import numpy as np
import os
import folium

# Load data

diphtheria = pd.read_csv('./data/disease/diphtheria.csv', index_col= 0, header=1)
measles = pd.read_csv('./data/disease/measles.csv', index_col=0, header=1)
mumps = pd.read_csv('./data/disease/mumps.csv', index_col=0, header=1)
neonatal_tetanus = pd.read_csv('./data/disease/neonatal_tetanus.csv', index_col=0, header=1)
tuberculosis = pd.read_csv('./data/disease/tuberculosis.csv', index_col=0, header=1)


html = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
geo_data = h.extract_json_html(html)

world_map = folium.Map(tiles='Stamen Toner', zoom_start=7)
world_map.choropleth(geo_data=geo_data)
world_map.save("mymap.html")