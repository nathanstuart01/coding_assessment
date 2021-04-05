import pandas as pd
import math
import sqlite3

def create_df(file_path, columns: list, sep='\t'):
    df = pd.read_csv(file_path, usecols=columns, sep=sep)
    return df

def merge_dfs(df_1, df_2, left_on='tconst', right_on='tconst'):
    merged_df = df_1.merge(df_2, left_on=left_on, right_on=right_on)
    return merged_df

def process_genres_counts(genre):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute(f"select count(*) from basics_data where genres='{genre}'")
    rows = cur.fetchall()
    rows = rows[0][0]
    if rows >= 0:
        return rows
    else:
        return 'Provided genre does not exist in movie data'

def get_movie_rating(title, data_file_paths: dict, data_columns: dict):
    df_1 = create_df(data_file_paths['basics_data_loc'], data_columns['basics_data_cols_ratings_titles'])
    df_1 = df_1[df_1.titleType == 'movie']
    df_2 = create_df(data_file_paths['ratings_data_loc'], data_columns['ratings_data_cols'])
    merged_df = merge_dfs(df_1, df_2)
    values = merged_df.loc[merged_df['primaryTitle'] == f'{title}']
    if len(values) == 0:
        return 'Provided movie title does not exist in movie data'
    values = values[['primaryTitle', 'averageRating']]
    avg_rating = sum(list(values['averageRating'].values)) / len(list(values['averageRating'].values))
    if math.isnan(avg_rating) == True:
        return 'Provided movie title does not have an average rating'
    return avg_rating

def get_top_rated_title_genre(genre, data_file_paths: dict, data_columns: dict):
    df_1 = create_df(data_file_paths['basics_data_loc'], data_columns['basics_data_cols_ratings_titles'])
    df_1 = df_1[df_1.titleType == 'movie']
    df_1['genres'] = df_1['genres'].apply(lambda x: x.split(','))
    df_1 = df_1.explode('genres')
    df_2 = create_df(data_file_paths['ratings_data_loc'], data_columns['ratings_data_cols'])
    df_3 = merge_dfs(df_1, df_2)
    df_3 = df_3.loc[df_3['genres'] == f'{genre}']
    df_3 = df_3.loc[df_3['averageRating'] == df_3.groupby(['genres']).agg({'averageRating':'max'}).values[0][0]]
    titles = list(df_3.primaryTitle.values)
    return titles

