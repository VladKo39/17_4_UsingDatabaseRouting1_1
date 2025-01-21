from fastapi import FastAPI
from app.routers import task, user

app=FastAPI()

app.include_router(task.router)
app.include_router(user.router)

@app.get('/')
async def welcome():
    return ({"message": "Welcome to Taskmanager1"})


'''
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
Маршруты:
В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/',
по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
'''