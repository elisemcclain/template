from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    genre = Column(String())
    
    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name}'
    


class Field(Base):
    __table__ = "field"
    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    location = Column(String())
    #times = Column(Integer())

    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name},' \
            + f'Location: {self.location}' 


class Festival(Base):
    __table__ = "festival"
    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    #times = Column(Integer())

    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name},' \
            + f'Start_date: {self.start_date},' \
            + f'End_date: {self.end_date}'

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()