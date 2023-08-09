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
    time = Column(String())
    festivals = relationship('Festival', secondary=festival_artist, back_populates='artists')
    def __repr__(self):
        return f'Id: {self.id},' \
            + f'Name: {self.name}' \
            # + f'Genre: {self.genre}'
    
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
            
if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # manually setting up data for db
    # if db being annoying, just delete both db files and run models.py again, db will be recreated
        # or run updates (CRUD)
        
    #tuples
    dates_list = ('2023-08-11', '2023-08-12', '2023-08-13')
    # dates_list[0]
    t1 = '6:30 pm'
    t2 = '7:30 pm'
    t3 = '8:30 pm'
    
    # coachella = Festival(name="Coachella", day_one=d1, day_two=d2, day_three=d3)
    # session.add(coachella)
    # session.commit()
        # create instance of festival, day1-3 placeholder properties for now
    
    
    rex = Artist(name='Rex Orange County', stage=1, time=t1, day_perform = dates_list[0])
    wknd2 = Artist(name='The Weeknd', stage=2, time=t1, day_perform = dates_list[0])
    zedd2 = Artist(name='Zedd', stage=1, time=t2, day_perform = dates_list[0])
    gryf2 = Artist(name='Gryffin', stage=2, time =t2, day_perform = dates_list[0])
    
    rex2 = Artist(name='Rex Orange County', stage=1, time=t1, day_perform= dates_list[1])
    ari = Artist(name='Ariana Grande', stage=1, time=t2, day_perform = dates_list[1])
    ari2 = Artist(name='Ariana Grande', stage=1, time=t3, day_perform = dates_list[1])
    zedd = Artist(name='Zedd', stage=2, time=t1, day_perform = dates_list[1])
    
    wknd = Artist(name='The Weeknd', stage = 1, time=t1, day_perform = dates_list[2])
    ari3 = Artist(name='Ariana Grande', stage=1, time=t3, day_perform = dates_list[2])
    khalid = Artist(name='Khalid', stage=1, time =t2, day_perform = dates_list[2])
    khalid2 = Artist(name='Khalid', stage=2, time =t3, day_perform = dates_list[2])
    gryf = Artist(name='Gryffin', stage=2, time =t2, day_perform = dates_list[2])
    
    
    
    
    coachella = session.query(Festival).filter_by(name='Coachella').first()
    # coachella.artists.extend([rex2,ari2,ari3,wknd2,zedd2,khalid2,gryf2])
    # extend = append iterables
    # append artists to festival selected using query 
    
    # artists = session.query(Artist).first()
    # print(artists.name)
    # session.commit()

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