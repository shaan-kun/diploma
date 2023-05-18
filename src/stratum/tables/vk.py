from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class VKUser(Base):
    __tablename__ = 'vk_users'

    user_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    domain = Column(String, unique=True, nullable=True)
    name = Column(String)
    type = Column(String)


class Wall(Base):
    __tablename__ = 'walls'

    wall_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    user_id = Column(Integer, ForeignKey('vk_users.user_id'), index=True)
    content = Column(String, nullable=True)
    date = Column(Date)
    likes = Column(Integer)
    shared = Column(Integer)
    views = Column(Integer)
    comments = Column(Integer)
