import sqlite3
import os
import classes as c

# Get root project path i.g: C:/Users/Documents/Project
dir_path = os.path.dirname(__file__)
# Create database in C:/Users/Documents/Project/wow.db
db_url = dir_path + '/'

def get_db_path():
    return dir_path

def get_connection(db_name = 'database.db'):
    return sqlite3.connect(db_url + db_name)

def create_database():
    conn = get_connection()
    cursor = conn.cursor()
# creating the databse 

    try:
        # Create table iten
        cursor.execute("""
        CREATE TABLE iten(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name INTEGER NOT NULL,
            description CHAR NOT NULL,
            con FLOAT NOT NULL,
            str FLOAT NOT NULL,
            int FLOAT NOT NULL,
            spd FLOAT NOT NULL
        );
        """)

    except sqlite3.Error as e:
        print('iten error:',e)

    try:
        # Create table race
        cursor.execute("""
        CREATE TABLE race(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name INTEGER NOT NULL,
            con FLOAT NOT NULL,
            str FLOAT NOT NULL,
            int FLOAT NOT NULL,
            spd FLOAT NOT NULL
        );
        """)

    except sqlite3.Error as e:
        print('race error:',e)

    try:
        # Create table class
        cursor.execute("""
        CREATE TABLE class(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name INTEGER NOT NULL,
            con FLOAT NOT NULL,
            str FLOAT NOT NULL,
            int FLOAT NOT NULL,
            spd FLOAT NOT NULL
        ); 
        """)

    except sqlite3.Error as e:
        print('class error:',e)

    try:

        # Create table player
        cursor.execute("""
        CREATE TABLE player(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name CHAR(45) NOT NULL,
            level int NOT NULL,
            exp FLOAT NOT NULL,
            id_class INT NOT NULL,
            id_race INT NOT NULL,
            life FLOAT NOT NULL,
            mana FLOAT NOT NULL,
            con FLOAT NOT NULL,
            str FLOAT NOT NULL,
            int FLOAT NOT NULL,
            spd FLOAT NOT NULL,

            FOREIGN KEY (id_race) REFERENCES race(id),
            FOREIGN KEY (id_class) REFERENCES class(id)
        );
        """)
    except sqlite3.Error as e:
        print('player error:',e)


    try:
        # Create table storage
        cursor.execute("""
        CREATE TABLE storage(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_iten INTEGER NOT NULL,
            id_player INTEGER NOT NULL,

            FOREIGN KEY (id_iten) REFERENCES iten(id),
            FOREIGN KEY (id_player) REFERENCES player(id)
        );
        """)

    
    except sqlite3.Error as e:
        print('storage error:',e)
        
        
    conn.close()

def create_class(clas):
    conn = get_connection()

    conn.execute(f"INSERT INTO class(name, con, str, int, spd) VALUES( '{clas.name}', '{clas.con}', '{clas.str}', '{clas.int}', '{clas.spd}');")
    conn.commit()
    conn.close()    

def create_race(race):
    conn = get_connection()

    conn.execute("""INSERT INTO race VALUES (""",
    race.id, ',',
    race.name, ',',
    race.con, ',',
    race.str, ',',
    race.int, ',',
    race.spd, ');')

    conn.close() 

def create_player(player):
    conn = get_connection()

    conn.execute("""INSERT INTO player VALUES (""",
    player.id, ',',
    player.name, ',',
    player.id_class, ',',
    player.id_race, ',',
    player.life, ',',
    player.mana, ',',
    player.con, ',',
    player.str, ',',
    player.int, ',',
    player.spd, ');')

    conn.close()    
