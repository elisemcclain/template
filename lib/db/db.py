from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Artist, Field
# from functions import test

# Database setup

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def create_session():
        return Session()
    
    print('hi dead world')
    
    # test()
    
    sza = Artist(name="SZA")
    f1 = Stage(name="Moonlight Stage", location = "South")
    session.add(sza)
    session.add(f1)
    session.commit()

    all_artists = session.query(Artist).all()
    for artist in artists:
        print(f'Artist: {artist.name}')
        for stage in artist.stage:
            print(f'Stage: {stage.name}')

