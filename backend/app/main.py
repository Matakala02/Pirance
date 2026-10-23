from fastapi import FastAPI

from app.routers import health

app = FastAPI(title="Finance API")
app.include_router(health.router)