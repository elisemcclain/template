from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    
    def __repr__(self):
        return f'Id: {self.id},' \
            f'Name: {self.name}'

class Field(Base):
    __tablename__ = "field"
    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    location = Column(String())
    


