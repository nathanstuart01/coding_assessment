import unittest
import os
from unittest.mock import patch
import pandas as pd
from app import create_app
from app.business_logic.helper_functions import *

class TestHelperFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_app = create_app('development')
        cls.test_data_file_paths = cls.test_app.config['DATA_FILE_PATHS']
        cls.test_data_columns = cls.test_app.config['DATA_FILE_COLUMNS']

    def test_create_df(self):
        test_df = create_df(self.test_data_file_paths['basics_data_loc'], self.test_data_columns['basics_data_cols_genre'])
        self.assertEqual(str(type(test_df)), "<class 'pandas.core.frame.DataFrame'>")

    def test_merge_dfs(self):
        test_df_1 = create_df(self.test_data_file_paths['basics_data_loc'], self.test_data_columns['basics_data_cols_genre'])
        test_df_2 = create_df(self.test_data_file_paths['ratings_data_loc'], self.test_data_columns['ratings_data_cols'])
        test_merge_dfs = merge_dfs(test_df_1, test_df_2)
        self.assertEqual(test_merge_dfs.columns.values.tolist(), ['tconst', 'titleType', 'genres', 'averageRating'])

    def test_process_genres_counts(self):
        test_genre_count = process_genres_counts('Comedy', self.test_data_file_paths['basics_data_loc'], self.test_data_columns['basics_data_cols_genre'])
        self.assertEqual(test_genre_count, 2)

    def test_process_missing_genres_counts(self):
        test_missing_genre_count = process_genres_counts('Dragons', self.test_data_file_paths['basics_data_loc'], self.test_data_columns['basics_data_cols_genre'])
        self.assertEqual(test_missing_genre_count, 'Provided genre does not exist in movie data')

    def test_get_movie_rating(self):
        test_title = 'Blacksmith Scene'
        test_movie_rating = get_movie_rating(test_title, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_movie_rating, 6.1)

    def test_get_avg_movie_rating_multiple(self):
        test_title = 'Carmencita'
        test_movie_rating = get_movie_rating(test_title, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_movie_rating, 5.75)

    def test_get_avg_movie_rating_no_title(self):
        test_title = 'Top Gun'
        test_movie_rating = get_movie_rating(test_title, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_movie_rating, 'Provided movie title does not exist in movie data')

    def test_get_avg_movie_rating_no_rating(self):
        test_title = 'Frozen'
        test_movie_rating = get_movie_rating(test_title, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_movie_rating, 'Provided movie title does not have an average rating')

    def test_get_top_rated_title_genre(self):
        test_genre ='Short'
        test_top_rated_movie = get_top_rated_title_genre(test_genre, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_top_rated_movie, ['Blacksmith Scene'])

    def test_get_top_rated_titles_genre(self):
        test_genre ='Sci-Fi'
        test_top_rated_movie = get_top_rated_title_genre(test_genre, self.test_data_file_paths, self.test_data_columns)
        self.assertEqual(test_top_rated_movie, ['The Dark Tower', 'Dune'])





