from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
#from ????? import backref


Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer, primary_key = True)
    name = Column(String())
    genre = Column(String())

    #foreign key for festival
    festival_id = Column(Integer, ForeignKey("festival.id"))
    festival = relationship("Festival", backref="performing_artists")
    
    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name}' \
            + f'Genre: {self.genre}'
    


class Stage(Base):
    __tablename__ = "stages"
    # __table_args__ = (PrimaryKeyConstraint('id'))

    id = Column(Integer, primary_key = True)
    name = Column(String())
    location = Column(String())
    #times = Column(Integer())

    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name},' \
            + f'Location: {self.location}' 

class Festival(Base):
    __tablename__ = "festival"
    # __table_args__= (PrimaryKeyConstraint('id'))

    id = Column('id', Integer, primary_key = True)
    name = Column(String())
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    #times = Column(Integer())

    #parent
    artists = relationship("Artist", backref="festival")
    #double check if artists is singular or plural

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