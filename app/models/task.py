from app.backend.db import Base
# импортируется класс Base из модуля app.backend.db
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
## relationship позволяет связать объекты друг с другом при создании, и SQLAlchemy
# автоматически определит, к каким записям они относятся.
from sqlalchemy.schema import CreateTable
# генерация оператора CREATE TABLE в SQLAlchemy
from app.models import user

class Task(Base):
    __tablename__ = 'tasks'    # задаёт название таблицы для модели в базе данных
    __table_args__ = {'extend_existing': True}

    id=Column(Integer,primary_key=True, index=True)
    # определение столбца id в SQLAlchemy, который будет представлять первичный ключ и иметь индекс.
    title=Column(String)
    # определение столбца в SQLAlchemy, представляет собой строку
    content=Column(String)
    # определение столбца в SQLAlchemy, представляет собой строку
    priority=Column(Integer,default=0)
    # определение столбца в SQLAlchemy, представляет собой число по умолчанию 0
    completed=Column(Boolean,default=False)
    # определение столбца в SQLAlchemy, представляет собой булево по умолчанию False
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    # определение столбца в SQLAlchemy, представляет собой число,является внешним ключём
    slug = Column(String,unique=True, index=True)
    # определение столбца, представляет строку, уникально, имеет индекс

    user= relationship('User', back_populates='tasks')
    # устанавливает связь между User и Task,
    # где параметр back_populates указывает,
    # что в модели Task будет соответствующий атрибут, который ссылается на модель User.

#print(CreateTable(Task.__table__))
