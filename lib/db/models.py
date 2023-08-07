from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class Artist(Base):
    __tablename__ = "artists"
    id = Column('id', primary_key = True)
    name = Column(String())


