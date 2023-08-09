# Script to seed initial data

from models import Artist, Festival, Genre, Base, festival_artist
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    #delete methods to clear database before each seeding
    # session.query(Artist).delete()
    # session.query(Festival).delete()
    # session.query(festival_artist).delete()

# manually setting up data for db
# if db being annoying, just delete both db files and run models.py again, db will be recreated
    # or run updates (CRUD)

#tuples
    dates_list = ('2023-08-11', '2023-08-12', '2023-08-13')
    dates_list2 = ('2024-08-04', '2024-08-05', '2024-08-06')
    # dates_list[0]
    t1 = '6:30 pm'
    t2 = '7:30 pm'
    t3 = '8:30 pm'
    
    # flatfest = Festival(name="Flatfest", day_one=dates_list[0], day_two=dates_list[1], day_three=dates_list[2])
    # flatfest2 = Festival(name="Flatfest 2.0", day_one=dates_list2[0], day_two=dates_list2[1], day_three=dates_list2[2])
    # session.add(flatfest)
    # session.commit()
        # create instance of festival, day1-3 placeholder properties for now

    #genres
    # gen1 = "Indie Pop"
    # gen2 = "R&B, Pop"
    # gen3 = "EDM"
    
    gen1 = Genre(genre = "Indie Pop")
    gen2 = Genre(genre = "R&B Pop")
    gen3 = Genre(genre = "EDM")
    
    rex = Artist(name='Rex Orange County', stage=1, time=t1, day_perform = dates_list[0], genre = gen1)
    zedd2 = Artist(name='Zedd', stage=1, time=t2, day_perform = dates_list[0], genre = gen3)
    ella = Artist(name='Ella Mai', stage=1, time =t3, day_perform = dates_list[0], genre = gen1)
    bruno = Artist(name='Bruno Mars', stage=2, time =t1, day_perform = dates_list[0], genre = gen2)
    wknd2 = Artist(name='The Weeknd', stage=2, time=t2, day_perform = dates_list[0], genre = gen2)
    gryf2 = Artist(name='Gryffin', stage=2, time =t3, day_perform = dates_list[0], genre = gen3)
    
    
    rex2 = Artist(name='Rex Orange County', stage=1, time=t1, day_perform= dates_list[1], genre = gen1)
    ari = Artist(name='Ariana Grande', stage=1, time=t2, day_perform = dates_list[1], genre = gen2)
    ari2 = Artist(name='Ariana Grande', stage=1, time=t3, day_perform = dates_list[1], genre = gen2)
    dhruv = Artist(name='dhruv', stage=2, time=t1, day_perform = dates_list[1], genre = gen2)
    zedd = Artist(name='Zedd', stage=2, time=t2, day_perform = dates_list[1], genre = gen3)
    west = Artist(name='Weston Estate', stage=2, time=t3, day_perform= dates_list[1], genre = gen1)

    
    wknd = Artist(name='The Weeknd', stage = 1, time=t1, day_perform = dates_list[2], genre = gen2)
    orange = Artist(name='Emotional Oranges', stage=1, time =t2, day_perform = dates_list[2], genre = gen2)
    ari3 = Artist(name='Ariana Grande', stage=1, time=t3, day_perform = dates_list[2], genre = gen2)
    drag = Artist(name='Imagine Dragons', stage=1, time=t1, day_perform = dates_list[2], genre = gen2)
    gryf = Artist(name='Gryffin', stage=2, time =t2, day_perform = dates_list[2], genre = gen3)
    khalid = Artist(name='Khalid', stage=2, time =t3, day_perform = dates_list[2], genre = gen2)
    
    

    flatfest = session.query(Festival).filter_by(name='Flatfest').first()
    flatfest.artists.extend([rex, zedd2, ella, bruno, wknd2, gryf2, rex2, ari, ari2, dhruv, zedd, west, wknd, orange, ari3, drag, gryf, khalid])
    # extend = append iterables
    # append artists to festival selected using query 
    
    # artists = session.query(Artist).first()
    # print(artists.name)
    session.commit()