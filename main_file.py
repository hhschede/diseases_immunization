# Import modules

import helpers as h
import pandas as pd
import numpy as np
import os

# Load data
for filename in os.listdir('./data/disease'):
    if filename[0] != '.':
        name = filename[:-4]
        print(name)
        name = pd.read_csv('./data/disease/' + filename)
        print(name.shape)

# diptheria = pd.read_csv('./data/disease/diphtheria.csv')
html = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
json_data = h.extract_json_html(html)
