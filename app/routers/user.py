from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import *
from app.schemas import CreateUser,UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify


router=APIRouter(prefix='/user',tags=['user'])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    #Метод scalars() преобразует результат select(User) в объекты модели,
    # а метод all() извлекает все результаты и возвращает их в виде списка
    return users


@router.get('/user_id')
async def user_by_id( db: Annotated[Session, Depends(get_db)],user_id: int):
    user = db.scalars(select(User).where (User.id==user_id))

    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {user_id} was not found')
    return user

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(
        insert(User).values(
            username=create_user.username,
            firstname=create_user.firstname,
            lastname=create_user.lastname,
            age=create_user.age,
            slug=slugify(create_user.username)
        )
    )
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)],user_id:int,update_user: UpdateUser):
    user=db.scalars(select(User).where(User.id==user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {user_id} was not found'
        )

    db.execute(
    update(User).values(
        username=update_user.username,
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age,
        slug = slugify(update_user.username)
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.delete('/delete')
async def delete_user( db: Annotated[Session, Depends(get_db)],user_id: int):
    user = db.scalars(select(User).where (User.id)==user_id())

    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {user_id} was not found')
    return user
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


