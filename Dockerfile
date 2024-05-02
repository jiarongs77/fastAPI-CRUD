FROM python:3.11

ENV POETRY_VERSION=1.6.1 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
RUN curl -sSL 'https://install.python-poetry.org' | python - \
  # https://github.com/python-poetry/poetry
  && poetry --version

WORKDIR /app

# Copy only requirements, to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml /app/
RUN poetry install

COPY . /app
COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
