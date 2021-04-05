#!/bin/bash
exec gunicorn -b :5000 --access-logfile logs/movie_app.log --error-logfile logs/movie_app.log run:app
