import os
import pandas as pd
import sqlite3
from flask import current_app

def populate_movies_data():
    root_dir = os.path.abspath(os.curdir)
    basics_data_source = f'{root_dir}/basics_data.tsv'
    basics_headers = ['tconst', 'titleType', 'primaryTitle', 'genres']
    basics_data = pd.read_csv(basics_data_source, usecols=basics_headers, sep='\t')
    basics_data = basics_data[basics_data.titleType == 'movie']
    basics_data['genres'] = basics_data['genres'].apply(lambda x: x.split(','))
    basics_data = basics_data.explode('genres')

    ratings_data_source = f'{root_dir}/ratings_data.tsv'
    ratings_headers = ['tconst','averageRating']
    ratings_data = pd.read_csv(ratings_data_source, usecols=ratings_headers, sep='\t')

    if os.path.exists('movies.db'):
        os.remove('movies.db')

    conn = sqlite3.connect('movies.db')

    basics_data.to_sql('basics_data', conn, dtype={
        'tconst': 'VARCHAR(256)',
        'titleType': 'VARCHAR(256)',
        'primaryTitle': 'VARCHAR(256)',
        'genres': 'VARCHAR(256)'
    })

    ratings_data.to_sql('ratings_data', conn, dtype={
        'tconst': 'VARCHAR(256)',
        'averageRating': 'VARCHAR(256)'
    })
