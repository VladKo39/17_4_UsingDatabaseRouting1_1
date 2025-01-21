from app.backend.db import Base
# импортируется класс Base из модуля app.backend.db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# relationship позволяет связать объекты друг с другом при создании, и SQLAlchemy
# # автоматически определит, к каким записям они относятся.
# from app.models import task
from sqlalchemy.schema import CreateTable
# # генерация оператора CREATE TABLE в SQLAlchemy

class User(Base):
    __tablename__ = 'users'
    # задаёт название таблицы для модели User в базе данных
    __table_args__ = {'extend_existing': True}

    id=Column(Integer,primary_key=True, index=True)
    # определение столбца id, представляет первичный ключ и иметь индекс.
    username = Column(String)
    # определение столбца
    firstname = Column(String)
    # определение столбца
    lastname = Column(String)
    # определение столбца
    age = Column(Integer)
    # определение столбца
    slug = Column(String, unique=True, index=True)
    # определение столбца, представляет строку, уникально, имеет индекс

    tasks = relationship('Task', back_populates='user', cascade='save-update, merge, delete')

    #, cascade='save-update, merge, delete'


#print(CreateTable(User.__table__))