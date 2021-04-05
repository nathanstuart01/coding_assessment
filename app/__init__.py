#This file initializes application and brings together all of the various components.
from flask import Flask
import logging
from config import configs
import pandas as pd

def create_app(config='default'):
    app = Flask(__name__)
    #basics_df = pd.read_csv('/Users/nathanstuart/work_code/flask_app/basics_data.tsv', usecols=['tconst', 'titleType', 'genres'], sep='\t')
    #basics_df = basics_df[basics_df.titleType == 'movie']
    #app.basics_df = basics_df
    app.config.from_object(configs[config])
    log_level = app.config['LOG_LEVEL']
    log_file = app.config['LOG_FILE']
    logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s %(name)s: %(message)s')

    with app.app_context():
        from .routes import routes

    return app

