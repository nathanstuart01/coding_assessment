import os, logging, json
from flask import request, jsonify, current_app
from app.business_logic.helper_functions import process_genres_counts, get_movie_rating, get_top_rated_title_genre

logger = logging.getLogger('routes_logger')

DATA_FILE_PATHS = current_app.config['DATA_FILE_PATHS']
DATA_COLUMNS = current_app.config['DATA_COLUMNS']

@current_app.route('/count_movie_titles_genres', methods=['GET'])
def get_count_movie_titles_genre():
    data = json.loads(request.data)
    genre = data['genre']
    genre_count = process_genres_counts(genre)
    return jsonify({'Genre': genre, 'Count Movie Titles': genre_count}), 200

@current_app.route('/get_movie_title_rating', methods=['GET'])
def get_movie_title_rating():
    data = json.loads(request.data)
    title = data['title']
    movie_rating = get_movie_rating(title, DATA_FILE_PATHS, DATA_COLUMNS)
    return jsonify({'Title': title, 'Avg Rating': movie_rating }), 200

@current_app.route('/get_top_rated_movie_genre', methods=['GET'])
def get_top_rated_movie_title_genre():
    data = json.loads(request.data)
    genre = data['genre']
    top_rated_title = get_top_rated_title_genre(genre, DATA_FILE_PATHS, DATA_COLUMNS)
    return jsonify({'Genre': genre, 'Top Rated Title(s)': top_rated_title}), 200