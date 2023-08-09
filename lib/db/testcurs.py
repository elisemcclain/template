import sqlite3, os, time, sys
from pyfiglet import Figlet
conn = sqlite3.connect('concert_app.db')
cursor = conn.cursor()
# cursor.execute("SELECT * FROM artists WHERE stage = 2")
# rows = cursor.fetchall()
# for row in rows:
#     print(row[1])
    
user_input = ""
f = Figlet(font='smslant')
d = Figlet(font='doom')
small = Figlet(font='small')
# http://www.figlet.org/examples.html ---> figlet fonts
# print(f)
# print('Welcome to FlatFest!! \n 1. Festival Dates \n 2. Find Field \n 3. Find Artist')
# print(Figlet().getFonts())
# print()
names = ['BROUGHT TO YOU BY', 'ELISE', 'MEGAN', 'SAM']
for i in names:
    print(d.renderText(i)),
    sys.stdout.flush()
    time.sleep(0.75)
# def second_input_func(second_input):
#     while second_input not in ['back', 'b']:
#         second_input = input()
#         if second_input == '1':
                
#             cursor.execute("SELECT name FROM artists WHERE")
#             for row in cursor.fetchall():
#                 print(row[0])
    
        
                    
while user_input not in ["quit", "q"]:
    user_input = input(f.renderText('Welcome to FlatFest ! !') + 'Type a number to continue: \n 1. Festival Dates \n 2. Details by Artist \n (Type "quit" or "q" to exit) \n')
    if user_input == "1":
        cursor.execute("SELECT day_perform FROM artists")
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
            print(small.renderText(dates[int(second_input)]))
            for row in sorted(set(cursor.fetchall())):
                print(small.renderText(row[0]))
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
            print(small.renderText(artists[int(second_input)]))
            for row in sorted(set(cursor.fetchall())):
                print(f'Stage {row[3]} at {row[4]} on {row[2]}')
            second_input = input('\nFind showtimes for any artist: \n (Type "back" or "b" to return) \n' + str)
            pass
    else:
        if user_input in ['quit', 'q']:
            exit()
        print(small.renderText("Invalid input"))
        time.sleep(1)
        user_input = input(f.renderText('Welcome to FlatFest ! !') + 'Type a number to continue: \n 1. Festival Dates \n 2. Details by Artist \n (Type "quit" or "q" to exit) \n')

    # elif user_input == "3":
    #     pass
    # elif user_input == '4':
    #     pass
        #
        

# print("hello " + input)
conn.close()