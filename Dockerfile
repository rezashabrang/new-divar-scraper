FROM python:3.8-slim
WORKDIR /app
# set environment variables
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="${PATH}:/root/.poetry/bin" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/penguin_api/ \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Tehran

# install dependencies
RUN apt update && apt upgrade -y && apt install curl make default-libmysqlclient-dev gcc -y

# POETRY
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
# RUN poetry lock -n && poetry export --without-hashes > requirements.txt
COPY ./pyproject.toml /app
COPY ./poetry.lock /app
RUN poetry install -n --only main

COPY . /app

# Final
WORKDIR /app
CMD python3 -m new_divar_scraper.main
