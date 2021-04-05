#This file initializes application and brings together all of the various components.
from flask import Flask
import logging
from config import configs
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database_config.sql_lite_config import populate_movies_data

db = SQLAlchemy()
migrate = Migrate()

def create_app(config='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    db.init_app(app)
    migrate.init_app(app, db)
    log_level = app.config['LOG_LEVEL']
    log_file = app.config['LOG_FILE']
    logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s %(name)s: %(message)s')

    with app.app_context():
        from .routes import routes
        from app.database_config.sql_lite_config import populate_movies_data
        populate_data = populate_movies_data()

    return app

