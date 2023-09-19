# FastAPI

## Get Started
1. Clone the repository
```bash
git clone git@github.com:eclipsegst/flask.git
```

2. Install dependencies
```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

3. Run the app
```bash
uvicorn app.main:app --reload
```
4. Check it
- http://127.0.0.1:8000
- API docs: 
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc

## Dependency Management
1. Add a new dependency to `pyproject.toml`
2. Run commands:
```bash
poetry lock
poetry install
```

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
