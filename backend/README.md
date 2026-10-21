# Zambia Personal Finance Platform: Backend

REST API for a personal finance app that helps people in Zambia track income
and expenses, manage debts and savings goals, and plan a budget.

**Backend:** Matakala | **Frontend:** Moffat

## Tech stack

- Python 3.14
- FastAPI
- PostgreSQL with SQLAlchemy and Alembic (migrations)
- JWT authentication

## Setup (Windows PowerShell)

1. Clone the repository and open the backend folder:

```
   git clone <repository-url>
   cd backend
```

2. Create and activate a virtual environment:

```
   python -m venv venv
   venv\Scripts\activate
```

3. Install the dependencies:

```
   pip install -r requirements.txt
```

4. Create a `.env` file (never commit it) with your own values:

```
   DATABASE_URL=postgresql://postgres:<password>@localhost:5432/finance_dev
   SECRET_KEY=<a long random string>
```

5. Start the server:

```
   uvicorn app.main:app --reload
```

## Using the API

- Health check: http://localhost:8000/health
- Interactive API docs: http://localhost:8000/docs

## Project status

- [x] Project setup and health check
- [ ] Database connection and migrations
- [ ] Register and login (JWT)
- [ ] Income, expenses, debts, savings goals, budget
- [ ] Dashboard and analysis

## Notes for the team

- Never commit `.env` or secrets.
- Work on a feature branch and open a pull request. Do not push directly to `main`.
- Any change to an endpoint or JSON shape must be agreed with the frontend developer first.
