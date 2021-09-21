FROM python:3.9.7-slim
ENV PYTHONUNBUFFERED=1

ENV HOME=/home/app
ENV APP_HOME=/home/app/movies
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/static
WORKDIR $APP_HOME


COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY movies ./movies
COPY movies_admin ./movies_admin
COPY manage.py .
COPY docker/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/home/app/movies/entrypoint.sh"]