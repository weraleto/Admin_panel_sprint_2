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

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "movies_admin.wsgi"]