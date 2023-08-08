# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from models import Base, Artist
# from functions import test

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///concert_app.db')
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
    

    # clairo = Artist(name="Clairo", genre="Alt/Indie")
    # tswizzle = Artist(name="TSwizzle", genre="Pop")
    # sza = Artist(name="SZA", genre="R&B")

    # session.bulk_save_objects([clairo, tswizzle, sza])
    # session.commit()

    # all_artists = session.query(Artist)
    # artist_names = [name for name in session.query(Artist.name)]
    # print(artist_names)