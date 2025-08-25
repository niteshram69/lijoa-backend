FROM python:3.11-slim
WORKDIR /code
# System deps
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
# Poetry
ENV POETRY_VERSION=1.8.3
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
COPY pyproject.toml poetry.lock* /code/
RUN poetry install --no-root
COPY . /code
EXPOSE 8000
