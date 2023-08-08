# Utility functions and business logic

from db import create_session
from models import Artist, Stage, Festival

def get_artists_with_performances():
    session = create_session()
    artists = session.query(Artist).all()
    session.close()
    return artists

def get_stages_with_performances():
    session = create_session()
    stages = session.query(Field).all()
    session.close()
    return Stages

def test():
    print('hello')

