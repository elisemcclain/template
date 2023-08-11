# Command-line interface using Click or argparse
# import click
# from db import create_session
import sqlite3, os, time, sys
from pyfiglet import Figlet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
engine = create_engine('sqlite:///concert_app.db')
Base.metadata.create_all(engine)
   
Session = sessionmaker(bind=engine)
session = Session()

conn = sqlite3.connect('concert_app.db')
cursor = conn.cursor()
user_input = ""
f = Figlet(font='smslant')
d = Figlet(font='doom')
small = Figlet(font='small')
# http://www.figlet.org/examples.html ---> figlet fonts
# print(f)
names = ['BROUGHT TO YOU BY', 'ELISE', 'MEGAN', 'SAM']
for i in names:
    print(f.renderText(i)),
    sys.stdout.flush()
    time.sleep(0.5)

dance_animation = ["0.txt", "1.txt", "2.txt", "3.txt", "4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt","11.txt", "12.txt", "13.txt","14.txt", "15.txt", "16.txt"]
reading = ["reading.txt","reading2.txt"]

def display_animations(filenames, delay=.05, repeat=4):
    frames = []
    for name in filenames:
        with open(name, 'r', encoding = 'utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(''.join(frame))
            time.sleep(delay)
            os.system('clear')

display_animations(dance_animation)


                    
while user_input not in ["quit", "q"]:

    user_input = input(f"\033[95m{d.renderText('Welcome to FlatFest ! !')}\033[0m" + 'Type a number to continue: \n 1. Festival Dates \n 2. Details by Artist \n 3. Details by Genre \n(Type "quit" or "q" to exit) \n')
    if user_input == "1":
        cursor.execute("SELECT day_perform FROM artists")
        #STORED INSIDE CURSOR.FETCHALL()

        i = 1
        str = ''
        dates =['0'] 
        for row in sorted(set(cursor.fetchall())):
            str += f'{i}. ' + row[0] + '\n'
            dates.append(row[0])
            i+=1
        second_input = input('\nFind all artists for that date: \n (Type "back" or "b" to return) \n' + str)
        while second_input not in ['back', 'b']:
            sql1 = "SELECT name FROM artists WHERE day_perform= ? "
            cursor.execute(sql1, (dates[int(second_input)],))
            print(f"\033[92m{small.renderText(dates[int(second_input)])}\033[0m")
            for row in sorted(set(cursor.fetchall())):
                print(f"\033[36m{small.renderText(row[0])}\033[0m")
            second_input = input('\nFind all artists for that date: \n (Type "back" or "b" to return) \n' + str)
            
    elif user_input == "2":
        cursor.execute("SELECT name FROM artists")
        artists =[''] 
        i = 1
        str = ''
        for row in sorted(set(cursor.fetchall())):
            str += f'{i}. ' + row[0] + '\n'
            artists.append(row[0])
            i+=1  
        second_input = input('\nFind showtimes for any artist: \n (Type "back" or "b" to return) \n' + str)
        while second_input not in ['back', 'b']:
            sql1 = "SELECT * FROM artists where name = ?"
            cursor.execute(sql1, (artists[int(second_input)],))
            print(f"\033[91m{small.renderText(artists[int(second_input)])}\033[0m")
            for row in sorted(set(cursor.fetchall())):
                print(f'Stage {row[3]} at {row[4]} on {row[2]}')
            second_input = input('\nFind showtimes for any artist: \n (Type "back" or "b" to return) \n' + str)
            # pass
    elif user_input == "3":
        cursor.execute("SELECT genre FROM genres")
        genres = ['']
        i = 1
        str = ''
        for row in sorted(set(cursor.fetchall())):
            str += f'{i}. ' + row[0] + '\n'
            genres.append(row[0])
            i+=1
        second_input=input('\nFind artists for any genre: \n (Type "back" or "b" to return) \n' + str)
        while second_input not in ['back', 'b']:
            sql1 = "SELECT name FROM artists WHERE genre_id = ?"
            cursor.execute(sql1, (int(second_input),))
            print(f"\033[94m{small.renderText(genres[int(second_input)])}\033[0m")

            for row in sorted(set(cursor.fetchall())):
                print(row[0])
            second_input = input('\nFind artists for any genre: \n (Type "back" or "b" to return) \n' + str)
    
    # elif user_input == '4':
    #     print('Festival name (e.g. Coachella)')
    #     sql1 = "INSERT INTO"
    #     second_
    
    else:
        if user_input in ['quit', 'q']:
            exit()
        print(small.renderText("Invalid input"))
        time.sleep(1)
        user_input = input(f.renderText('Welcome to FlatFest ! !') + 'Type a number to continue: \n 1. Festival Dates \n 2. Details by Artist \n 3. Details by Genre \n 4. Add New Performance \n (Type "quit" or "q" to exit) \n')

conn.close()



if __name__ == "__main__":
    main()









# from functions import get_artists_with_performances, get_stages_with_performances

# @click.command()
# def artists_command():
#     session = create_session()
#     artists = get_artists_with_performances(session)
#     session.close()

# @click.command()
# def stages_command():
#     session = create_session()
#     stages = get_stages_with_performances(session)
#     session.close()

# if __name__ == '__main__':
#     artists_command()
#     stages_command()