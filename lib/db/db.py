from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Artist
from functions import test

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print('test')
    
    test()
    
    asd = Artist(name="as")
    session.add(asd)
    session.commit()
