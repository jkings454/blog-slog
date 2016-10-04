from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = "post"
    content = Column(String(1000), nullable = False)
    title = Column(String(250), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id = Column(Integer, primary_key = True)

engine = create_engine(config.production["DB_URI"])
Base.metadata.create_all(engine)
