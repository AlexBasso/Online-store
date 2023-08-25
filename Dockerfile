FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app2

RUN pip install --upgrade pip "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN apt-get update && apt-get install -y git
RUN poetry install

COPY megano .
COPY diploma-frontend .


CMD ["gunicorn", "megano.wsgi:application", "--bind", "0.0.0.0:8000"]