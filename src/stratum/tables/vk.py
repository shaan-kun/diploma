from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Numeric,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class VKUser(Base):
    __tablename__ = 'vk_users'

    user_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    domain = Column(String, unique=True, nullable=True)
    first_name = Column(String)
    second_name = Column(String)
    last_name = Column(String)
    country = Column(String)
    city = Column(String)
    bdate = Column(Date)
    contacts = Column(String)


class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    screen_name = Column(String, unique=True, nullable=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    country = Column(String)
    city = Column(String)
    contacts = Column(String)


class SourceType(Base):
    __tablename__ = 'sourcetypes'

    sourcetype_id = Column(Integer, primary_key=True)
    name = contacts = Column(String)


class Source(Base):
    __tablename__ = 'sources'

    source_id = Column(Integer, primary_key=True)
    sourcetype_id = Column(Integer, ForeignKey('sourcetypes.sourcetype_id'), index=True)


class Following(Base):
    __tablename__ = 'followings'

    following_id = Column(Integer, primary_key=True)
    source_from = Column(Integer, ForeignKey('sources.source_id'), index=True)
    source_to = Column(Integer, ForeignKey('sources.source_id'), index=True)


class Wall(Base):
    __tablename__ = 'walls'

    wall_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    source_id = Column(Integer, ForeignKey('vk_users.user_id'), index=True)
    content = Column(String, nullable=True)
    date = Column(DateTime)
    likes = Column(Integer)
    shared = Column(Integer)
    views = Column(Integer)
    comments = Column(Integer)


class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('vk_users.user_id'), index=True)
    wall_id = Column(Integer, ForeignKey('walls.wall_id'), index=True)
    content = Column(String, nullable=True)
    date = Column(DateTime)
    likes = Column(Integer)
    replies = Column(Integer)


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    shname = Column(String)
    price = Column(Numeric(10, 2))
    about = Column(String)


class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    region = Column(String)
    address = Column(String)
    contacts = Column(String)


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    company_id = Column(Integer, ForeignKey('companies.company_id'), index=True)
    user_id = Column(Integer, ForeignKey('vk_users.user_id'), index=True)
    region = Column(String)
    address = Column(String)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'), index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), index=True)
    count = Column(Integer)
    address = Column(String)
    date = Column(DateTime)


class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('vk_users.user_id'), index=True)
    content = Column(String)
    date = Column(DateTime)
    attachment = Column(Boolean)
