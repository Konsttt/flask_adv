from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from db import engine
from sqlalchemy_utils import EmailType

Base = declarative_base(bind=engine)


class Adv(Base):
    __tablename__ = 'adv'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    message = Column(String)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("adv_users.id", ondelete="CASCADE"))
    user = relationship("User", lazy="joined")


class User(Base):

    __tablename__ = "adv_users"

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True, index=True)
    password = Column(String(60), nullable=False)
    registration_time = Column(DateTime, server_default=func.now())


Base.metadata.create_all()