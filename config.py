import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = os.getenv('LOG_FILE')
    LOG_LEVEL = 'INFO'
    ROOT_DIR = os.path.abspath(os.curdir)
    DATA_FILE_PATHS = {'basics_data_loc': f'{ROOT_DIR}' + '/basics_data.tsv', 'ratings_data_loc': f'{ROOT_DIR}' + '/ratings_data.tsv'}
    DATA_COLUMNS = {'basics_data_cols_genre': ['tconst', 'titleType', 'genres'],
                    'basics_data_cols_ratings_titles': ['tconst', 'titleType', 'primaryTitle', 'genres'],
                    'ratings_data_cols': ['tconst','averageRating']}

class ProductionConfig(Config):
    LOG_LEVEL = 'ERROR'
    DATEBASE_URI = 'prod database uri'
    SQLALCHEMY_DATABASE_URI = 'sqlalchemy prod database uri'
    LOG_LEVEL = 'ERROR'
    SECRET_KEY ='realy super secret key that no one would guess'

class DevelopmentConfig(Config):
    """
    DEBUG = True only enables debug mode, to fully enable the development environment:
    1.Set FLASK_ENV=development in .flaskenv
    2.Type: flask run in CLI and the flask development server will run with full stack tracing and error logging
    3. DO NOT SET FLASK_ENV=development in a production environment
    """
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    DATEBASE_URI = 'dev database uri'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.ROOT_DIR}/app.db'

    DATA_FILE_PATHS = {'basics_data_loc': f'{Config.ROOT_DIR}' + '/tests/test_data/test_basics_data.tsv',
                        'ratings_data_loc': f'{Config.ROOT_DIR}' + '/tests/test_data/test_ratings_data.tsv'}
    DATA_FILE_COLUMNS = Config.DATA_COLUMNS

configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': Config
}