from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Artist, Festival, Genre, Base)

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    # get festival artists
    festival = session.query(Festival).first()

    # use filter_by to get festival artists from Artist
    festival_artists = session.query(Artist).filter_by(id=owner.id)
    print([festival for festival in artist_festival])

