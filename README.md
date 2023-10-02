# FastAPI

## Get Started
1. Clone the repository
```bash
git clone git@github.com:eclipsegst/fastapi.git
```

2. Install dependencies
```bash
poetry lock
poetry install
```
Add a new dependency to `pyproject.toml`

3. Create `.env`

Here is an example,
```
SERVER_NAME=your_server_name
SERVER_HOST=http://localhost
PROJECT_NAME=your_project_name

FIRST_SUPERUSER=your_superuser_email@example.com
FIRST_SUPERUSER_PASSWORD=your_superuser_password

POSTGRES_SERVER=localhost:5432
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db_name

SMTP_PORT=587
SMTP_HOST=smtp.gmail.com
SMTP_USER=""
SMTP_PASSWORD=""
EMAILS_FROM_EMAIL="info@example.com"
```

4. Run the app
```
./run.sh
```
or
```bash
poetry run uvicorn app.main:app --reload
```
5. Check it
- http://127.0.0.1:8000
- API docs: 
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc

## Docker

1. Build image
```bash
docker build -t fastai-image .
```
2. Run a container

```bash
docker run -d --name fastai-container -p 80:80 fastai-image
```
3. Check it here: 
  - http://127.0.0.1
  - API docs: 
    - http://127.0.0.1/docs
    - http://127.0.0.1/redoc

## Notes
[1]: [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)

[2]: [uvicorn-gunicorn-fastapi-docker ](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/tree/master#quick-start)

[3]: [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master)
