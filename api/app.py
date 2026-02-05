from fastapi import FastAPI
from api.routes.accounts import router as accounts_router
from api.routes.expenses import router as expenses_router

app = FastAPI(title="Expense Management API")

@app.get("/")
def home():
    return {"message": "Expense & Finance Manager API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(accounts_router)
app.include_router(expenses_router)
