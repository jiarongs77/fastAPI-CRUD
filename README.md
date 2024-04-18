# FastAPI Base Project

This project aims to build a base project to build RESTful APIs for production application using FastAPI. It's highly inspired by [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master).

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) for Python backend API.
  - [Pydantic](https://docs.pydantic.dev/) for data validation and settings management.
  - PostgreSQL as the SQL database
  - [Alembic](https://github.com/sqlalchemy/alembic) for database migration
- Tests with [Pytest](https://docs.pytest.org/en/8.0.x/).

## Get Started

0. Prerequisite:

- Install Postgresql by following [Set up database](#set-up-database)
- Install [Poetry](https://python-poetry.org/docs/#installation). Poetry is a tool for dependency management and packaging in Python.
- Install [Postico 2](https://eggerapps.at/postico2/) for easily visualizing PostgreSQL tables.

1. Clone the repository

```bash
git clone git@github.com:eclipsegst/fastapi.git
```

2. Create `.env`

Copy `.env.example` and rename to `.env`, update the values. Make sure the database name is same as the one you set up in [Set up database](#set-up-database) and also in `setup.sh`.

```bash
cp .env.example .env
```

3. Configuration

Install dependencies and initial database migration

```bash
./setup.sh
```

4. Run the app

```
./run.sh
```

or

```bash
poetry run uvicorn app.main:app --reload
```

Note: `poetry run` will run under poetry virtualenv.

6. Check it

- http://127.0.0.1:8000
- API docs:
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc

Note: You might need to add `export PYTHONPATH=$(pwd):$PYTHONPATH` to `~/.bash_profile` if you get an error like "Cannot import or no app module".

## Run with Docker

1. Build image

```bash
docker build -t fastapi-image .
```

2. Run a container

```bash
docker run -d --name fastapi-container -p 80:80 fastapi-image
```

check container status,

```bash
docker logs -f fastapi-container
```

Some useful docker commands:

- docker container ls
- docker container stop container_id
- docker rm /fastapi-container
- docker image ls
- docker image rm image_id
- docker logs -f fastapi-container

3. Check it here:

- http://127.0.0.1
- API docs:
  - http://127.0.0.1/docs
  - http://127.0.0.1/redoc

## Manage dependencies

```bash
poetry lock
poetry install
```

Add a new dependency to `pyproject.toml`

## Set up database

Install postgresql

```
brew install postgresql
brew services start postgresql
brew services stop postgresql
```

Check if it's running

```
ps -ef | grep postgres
```

Create user with password

```
createuser -U postgres -W
```

Create database with name `fastapi_db`

```
createdb -U postgres -w fastapi_db
```

Set up initial data

```
./setup.sh
```

### Database Migration

Initial migration

```
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

Further Developing

```
alembic revision --autogenerate -m "description of your change"
alembic upgrade head
```

## Testing

For a simple local test, we need to set up a separate database for test, e.g. `fastapi_db_test`.

## Steps

- Change db name to `fastapi_db_test` in `.env`
- Run `./setup` to set up initial migration
- Create `.env.test.local` by copying `.env`
  - It will be loaded when running test in `app/core/config.py`
- Change back to original database name in `.env`
- Run `./scripts/test.sh`

Note: We can also use docker for setting up test environment.

## Notes

[1]: [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)

[2]: [uvicorn-gunicorn-fastapi-docker ](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/tree/master#quick-start)

[3]: [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master)

## License

FastAPI Base Project is licensed under the terms of the MIT license.
