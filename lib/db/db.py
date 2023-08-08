from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Artist, Field
from functions import test

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print('test')
    
    test()
    
    asd = Artist(name="as")
    f1 = Field(name="asd", location = "abc")
    session.add(asd)
    session.add(f1)
    session.commit()

#test test test 