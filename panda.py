import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame
import requests, zipfile
from io import StringIO
import io



# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# # Acquire data from the url
r = requests.get(url, stream=True)

# # read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

anime_data.head()