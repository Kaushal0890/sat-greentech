# Sat GreenTech Pvt. Ltd. Website

Modern solar company website built with Django for pages, admin, and content models, plus FastAPI for inquiry and listing endpoints mounted under `/api`.

## Stack

- Django 4.2
- FastAPI
- SQLite
- WhiteNoise

## Setup

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
python3 -m uvicorn config.asgi:application --reload
```

Open:

- Website: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- API Docs: `http://127.0.0.1:8000/api/docs`

## API Endpoints

- `POST /api/contact`
- `POST /api/quote`
- `GET /api/services`
- `GET /api/projects`
- `GET /api/brands`
# sat-greentech
