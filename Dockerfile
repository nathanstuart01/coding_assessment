FROM python:3.8

RUN adduser --disabled-password movie_app

WORKDIR /home/movie_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY tests tests
COPY logs logs
COPY .env config.py run.py boot.sh basics_data.tsv ratings_data.tsv ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R movie_app:movie_app ./
USER movie_app

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "./boot.sh" ]
