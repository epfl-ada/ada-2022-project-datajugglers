import os
import pandas as pd

# Script to construct IMDB data table from two raw tables

DATA_FOLDER = 'data'
IMDB_RATINGS_TABLE_PATH = os.path.join(DATA_FOLDER, 'title.ratings.tsv.gz')
IMDB_NAME_TABLE_PATH = os.path.join(DATA_FOLDER, 'title.basics.tsv.gz')
IMDB_FINAL_TABLE_PATH = os.path.join(DATA_FOLDER, 'imdb.ratings.tsv')

df_movies_IMDb_name = pd.read_csv(IMDB_NAME_TABLE_PATH, sep ='\t',\
    na_values = ['{}', ' '], lineterminator='\n')
df_movies_IMDb_ratings = pd.read_csv(IMDB_RATINGS_TABLE_PATH, sep ='\t',\
    na_values = ['{}', ' '], lineterminator='\n')

df_movies_IMDb_name = df_movies_IMDb_name[['tconst', 'originalTitle']]
df_IMDb_ex = df_movies_IMDb_ratings.merge(df_movies_IMDb_name, how ='inner', on=['tconst'])
df_IMDb_ex = df_IMDb_ex[['originalTitle', 'averageRating', 'numVotes']]
df_IMDb_ex = df_IMDb_ex.rename(columns={'originalTitle': 'movie name'})

df_IMDb_ex.to_csv(IMDB_FINAL_TABLE_PATH, sep='\t', index=False)
