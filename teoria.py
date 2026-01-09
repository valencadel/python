import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

import numpy as np

movies_90 = netflix_df[np.logical_and(netflix_df["release_year"] >= 1990, netflix_df["release_year"] < 2000)]
duration = int(np.mean(movies_90["duration"]))
print(duration)

movies_90_short = movies_90[np.logical_and(movies_90["duration"] < 90, movies_90["genre"] == "Action")]
short_movie_count = int(len(movies_90_short))
print(short_movie_count)