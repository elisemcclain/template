import sqlite3
conn = sqlite3.connect('concert_app.db')
cursor = conn.cursor()
# cursor.execute("SELECT name from artists")
# rows = cursor.fetchall()
# for row in rows:
#     print(row[0])
    
user_input = ""
# print('Welcome to FlatFest!! \n 1. Festival Dates \n 2. Find Field \n 3. Find Artist')
while user_input not in ["quit", "q"]:
    user_input = input('Welcome to FlatFest!! \n 1. Festival Dates \n 2. Find Field \n 3. Find Artist \n')
    if user_input == "1":
        # cursor.execute("SELECT name from artists")
        # replace
        rows = cursor.fetchall()
        i = 1
        for row in rows:
            print(f'{i}. ' + row[0])
            i += 1
    elif user_input == "2":
        second_input = ""
        print("now in 2, type back or b to return")
        while second_input not in ["back", "b"]:
            second_input = input()
            if second_input == "a":
                print("a in 2")
            
        pass
    elif user_input == "3":
        pass
        
# print("hello " + input)
conn.close()