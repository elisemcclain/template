# Command-line interface using Click or argparse

import click
from db import create_session
from functions import get_artists_with_performances, get_stages_with_performances

@click.command()
def artists_command():
    session = create_session()
    artists = get_artists_with_performances(session)
    session.close()

@click.command()
def stages_command():
    session = create_session()
    stages = get_stages_with_performances(session)
    session.close()

if __name__ == '__main__':
    artists_command()
    stages_command()