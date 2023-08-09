from sqlalchemy import Column, String, Integer, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

festival_artist = Table('festival_artists',
                        Base.metadata,
                        Column('festival_id', ForeignKey('festivals.id'), primary_key=True),
                        Column('artist_id', ForeignKey('artists.id'), primary_key=True),
                        extend_existing=True
                        )
                        
class Artist(Base):
    __tablename__ = "artists"
    id = Column('id', Integer, primary_key=True)
    name = Column(String())
    day_perform = Column(String())
    stage = Column(Integer())
    time = Column(String())
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship('Genre', back_populates='artists')
    festivals = relationship('Festival', secondary=festival_artist, back_populates='artists')
    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name}' 

class Genre(Base):
    __tablename__ = "genres"
    id = Column('id', Integer, primary_key=True)
    genre = Column(String())
    artists = relationship('Artist', back_populates='genres')
    def __repr__(self):
        return f'Id: {self.id}' \
        + f'Genre: {self.genre}'

    
class Festival(Base):
    __tablename__ = "festivals"
    id = Column('id', Integer, primary_key=True)
    name = Column(String())
    day_one = Column(String())
    day_two = Column(String())
    day_three = Column(String())
    artists = relationship('Artist', secondary=festival_artist, back_populates='festivals')
    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name},' \
            + f'Start_date: {self.day_one},' \
            + f'End_date: {self.day_three}'




# if __name__ == '__main__':
#     engine = create_engine('sqlite:///concert_app.db')
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()


# class Artist(Base):
#     __tablename__ = "artists"
#     __table_args__ = (PrimaryKeyConstraint('id'),)

#     id = Column(Integer, primary_key = True)
#     name = Column(String())
#     genre = Column(String())

#     #foreign key for festival
#     festival_id = Column(Integer, ForeignKey("festival.id"))
#     festival = relationship("Festival", backref="performing_artists")
    
    # def __repr__(self):
    #     return f'Id: {self.id},' \
    #         + f'Name: {self.name}' \
    #         + f'Genre: {self.genre}'
    


# class Stage(Base):
#     __tablename__ = "stages"
#     # __table_args__ = (PrimaryKeyConstraint('id'))

#     id = Column(Integer, primary_key = True)
#     name = Column(String())
#     location = Column(String())
#     #times = Column(Integer())

#     def __repr__(self):
#         return f'Id: {self.id},' \
#             + f'Name: {self.name},' \
#             + f'Location: {self.location}' 

# class Festival(Base):
#     __tablename__ = "festival"
#     # __table_args__= (PrimaryKeyConstraint('id'))

#     id = Column('id', Integer, primary_key = True)
#     name = Column(String())
#     start_date = Column(DateTime())
#     end_date = Column(DateTime())
#     #times = Column(Integer())

#     #parent
#     artists = relationship("Artist", backref="festival")
#     #double check if artists is singular or plural

#     def __repr__(self):
#         return f'Id: {self.id},' \
#             + f'Name: {self.name},' \
#             + f'Start_date: {self.start_date},' \
#             + f'End_date: {self.end_date}'

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///concert_app.db')
#     Base.metadata.create_all(engine)
    
#     Session = sessionmaker(bind=engine)
#     session = Session()