from fastapi import FastAPI
from router import router

app=FastAPI(title="Todo App with Mongodb")

app.include_router(router, prefix="/todos",tags=['Todos'])