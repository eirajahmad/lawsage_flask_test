# LawSage Flask Test

A tiny Flask + SQLAlchemy app that meets the three requirements.

## Endpoints

- `/` → HTML page: **"Welcome to LawSage Test"** (served via Jinja template)
- `/users` → JSON array of users from SQLite
- `/search?name=...` → Case-insensitive partial match on `name` or `email`

## Tech

- Flask
- SQLAlchemy + Flask-SQLAlchemy
- SQLite (file: `lawsage.db` auto-created on first run)
- Python 3.10+

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit http://localhost:8000/

```bash
# Get all users
curl -s http://localhost:5000/users | python -m json.tool

# Search (name or email, partial/ci)
curl -s "http://localhost:5000/search?name=ada" | python -m json.tool
```

## Notes

- The database is seeded with three users on first run if empty:
  - Ada Lovelace — `ada@lawsage.test`
  - Alan Turing — `alan@lawsage.test`
  - Grace Hopper — `grace@lawsage.test`

- `requirements.txt` is included per spec.
- Ready to push to GitHub (public or private).
```
git init
git add .
git commit -m "LawSage Flask test"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```
