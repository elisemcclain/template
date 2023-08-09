from sqlalchemy import Column, String, Integer, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

festival_artist = Table('festival_artists',
                        Base.metadata,
                        Column('festival_id', ForeignKey('festivals.id'), primary_key=True),
                        Column('artist_id', ForeignKey('artists.id'), primary_key=True),
                        # Column('genre_id', ForeignKey('genre.id'), primary_key=True),
                        extend_existing=True
                        )
# genre_artist = Table('genre_artists',
#                      Base.metadata,
#                      Column(),
#                      extend_existing=True
#                      )
# class Genre(Base):
#     __tablename__ = "genres"
#     id = Column('id', Integer, primary_key=True)
#     name = Column(String())
#     artists = relationship('Genre', back_populates='genres')
    
class Artist(Base):
    __tablename__ = "artists"
    id = Column('id', Integer, primary_key=True)
    name = Column(String())
    # genre = Column(Integer, ForeignKey('genres.id'))
    # genre = relationship('Genre', back_populates='artists')
    day_perform = Column(String())
    stage = Column(Integer())
    festivals = relationship('Festival', secondary=festival_artist, back_populates='artists')
    def __repr__(self):
        return 1
    
class Festival(Base):
    __tablename__ = "festivals"
    id = Column('id', Integer, primary_key=True)
    name = Column(String())
    day_one = Column(String())
    day_two = Column(String())
    day_three = Column(String())
    artists = relationship('Artist', secondary=festival_artist, back_populates='festivals')

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    d1 = '2023-08-11'
    d2 = '2023-08-12'
    d3 = '2023-08-13'
    t1 = '6:30 pm'
    t2 = '7:30 pm'
    t3 = '8:30 pm'
    
    ari = Artist(name='Ariana Grande', day_perform=d2, stage=1)
    zedd = Artist(name='Zedd', day_perform=d2, stage=2)
    
    
    # coachella = Festival(name="Coachella", day_one=d1, day_two=d2, day_three=d3)

    # associate artist with festival
    # f1.artists.append(asd)
    # session.add(coachella)
    
    coachella = session.query(Festival).filter_by(name='Coachella').first()
    coachella.artists.append(ari)
    
    
    session.commit()

# class Artist(Base):
#     __tablename__ = "artists"
#     __table_args__ = (PrimaryKeyConstraint('id'),)

#     id = Column(Integer, primary_key = True)
#     name = Column(String())
#     genre = Column(String())

#     #foreign key for festival
#     festival_id = Column(Integer, ForeignKey("festival.id"))
#     festival = relationship("Festival", backref="performing_artists")
    
#     def __repr__(self):
#         return f'Id: {self.id},' \
#             + f'Name: {self.name}' \
#             + f'Genre: {self.genre}'
    


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