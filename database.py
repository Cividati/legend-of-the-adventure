import sqlite3
import os
import classes as c
import pandas as pd

dir_path = os.path.dirname(__file__)

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
        print('races error:',e)

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

def create_race(race):
    conn = get_connection()

    conn.execute(f"INSERT INTO race(name, con, str, int, spd) VALUES( '{race.name}', '{race.con}', '{race.str}', '{race.int}', '{race.spd}');")
    conn.commit()
    conn.close()    

def create_class(clas):
    conn = get_connection()

    conn.execute(f"INSERT INTO class(name, con, str, int, spd) VALUES( '{clas.name}', '{clas.con}', '{clas.str}', '{clas.int}', '{clas.spd}');")
    conn.commit()
    conn.close() 

def create_iten(iten):
    conn = get_connection()

    conn.execute(f"INSERT INTO iten(name, description, con, str, int, spd) VALUES( '{iten.name}', '{iten.description}', '{iten.con}', '{iten.str}', '{iten.int}', '{iten.spd}');")
    conn.commit()
    conn.close() 


def create_player(player):
    conn = get_connection() 
    
    player.life += get_stats('race', 'con', player.id_race)*0.5 + get_stats('class', 'con', player.id_class)*0.5
    player.mana += get_stats('race', 'int', player.id_race)*0.5 + get_stats('class', 'int', player.id_class)*0.5
    player.con +=  get_stats('race', 'con', player.id_race) + get_stats('class', 'con', player.id_class)
    player.str += get_stats('race', 'str', player.id_race) + get_stats('class', 'str', player.id_class)
    player.int += get_stats('race', 'int', player.id_race) + get_stats('class', 'int', player.id_class)
    player.spd += get_stats('race', 'spd', player.id_race) + get_stats('class', 'spd', player.id_class)
    
    conn.execute(f"INSERT INTO player(name, level, exp, id_class, id_race, life, mana, con, str, int, spd) VALUES( '{player.name}', '{player.level}', '{player.exp}', '{player.id_class}', '{player.id_race}', '{player.life}', '{player.mana}', '{player.con}', '{player.str}', '{player.int}', '{player.spd}');")
    conn.commit()
    conn.close()    

def get_stats(tableName, stat, idName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT {stat} FROM {tableName} WHERE id = {idName};")
    
    rows = cur.fetchall()
    value = rows[0][0]

    return value

def get_player(value = '', param = 'name'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM player WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        player = c.player(
            rows[0][0],
            rows[0][1],
            rows[0][2],
            rows[0][3],
            rows[0][4],
            rows[0][5],
            rows[0][6],
            rows[0][7],
            rows[0][8],
            rows[0][9],
            rows[0][10],
            rows[0][11]
        )
        return player
    return False

def set_player(player):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'UPDATE player SET'
    f' name = "{player.name}",'
    f' level = "{player.level}",'
    f' exp = "{player.exp}",'
    f' id_class = "{player.id_class}",'
    f' id_race = "{player.id_race}",'
    f' life = "{player.life}",'
    f' mana = "{player.mana}",'
    f' con = "{player.con}",'
    f' str = "{player.str}",'
    f' int = "{player.int}",'
    f' spd = "{player.name}"'
    f' WHERE id = "{player.id}";')
    conn.commit()
