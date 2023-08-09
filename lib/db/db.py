from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Artist, Festival
from functions import test
from datetime import datetime
if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def create_session():
        return Session()
    
    # print('test')
    
    # test()
    
    asd = Artist(name="as", genre='123', day_perform = ' aa')
    # f1 = Field(name="asd", location = "abc")
    # session.add(asd)
    # session.add(f1)
    d1 = datetime(2023,8,11).strftime('%Y-%m-%d')
    d2 = datetime(2023,8,12).strftime('%Y-%m-%d')
    d3 = datetime(2023,8,13).strftime('%Y-%m-%d')
    # times = ['6:30pm', '7:30pm', '8:30pm']
    f1 = Festival(name="Coachella", day_one=d1, day_two=d2, day_three=d3)
    
    # test()
    
    sza = Artist(name="SZA")
    f1 = Stage(name="Moonlight Stage", location = "South")
    session.add(sza)
    session.add(f1)
    session.commit()
   
    
    # session.commit()
    
    
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


    