from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config


Base = declarative_base()

class Post(Base):
    __tablename__ = "post"
    content = Column(String(1000), nullable = False)
    title = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)

engine = create_engine(config.DB_URI)
Base.metadata.create_all(engine)
