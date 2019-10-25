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
       CREATE TABLE IF NOT EXISTS iten(
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
        CREATE TABLE IF NOT EXISTS race(
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
        CREATE TABLE IF NOT EXISTS class(
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
        CREATE TABLE IF NOT EXISTS player(
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
            iten_equipped INT

            FOREIGN KEY (iten_equipped) REFERENCES iten(id),
            FOREIGN KEY (id_race) REFERENCES race(id),
            FOREIGN KEY (id_class) REFERENCES class(id)
        );
        """)
    except sqlite3.Error as e:
        print('player error:',e)

    try:
        # Create table storage
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory(
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

    conn.execute(f"INSERT INTO race(name, con, str, int, spd) VALUES( "
        f"'{race.name}', '{race.con}', '{race.str}', '{race.int}', '{race.spd}');")
    conn.commit()
    conn.close()    

def create_class(clas):
    conn = get_connection()

    conn.execute(f"INSERT INTO class(name, con, str, int, spd) VALUES( "
        f"'{clas.name}', '{clas.con}', '{clas.str}', '{clas.int}', '{clas.spd}');")
    conn.commit()
    conn.close() 

def create_iten(iten):
    conn = get_connection()

    conn.execute(f"INSERT INTO iten(name, description, con, str, int, spd) VALUES( "
        f"'{iten.name}', '{iten.description}', '{iten.con}', '{iten.str}', '{iten.int}', '{iten.spd}');")
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
    
    conn.execute(f"INSERT INTO player(name, level, exp, id_class, id_race, life, mana, con, str, int, spd) VALUES(" 
        f"'{player.name}', '{player.level}', '{player.exp}', '{player.id_class}', '{player.id_race}',"
        f"'{player.life}', '{player.mana}', '{player.con}', '{player.str}', '{player.int}', '{player.spd}');")
    conn.commit()
    conn.close()    

def get_stats(tableName, stat, idName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT {stat} FROM {tableName} WHERE id = {idName};")
    
    rows = cur.fetchall()
    value = rows[0][0]

    return value

def get_iten(value = '', param = 'id'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM iten WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        iten = c.iten(
            rows[0][1],
            rows[0][2],
            rows[0][3],
            rows[0][4],
            rows[0][5],
            rows[0][6],
            rows[0][0]
        )
        return iten
    return False

def get_player(value = '', param = 'id'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM player WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        player = c.player(
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
            rows[0][11],
            rows[0][0]
        )
        return player
    return False

def get_class(value = '', param = 'id'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM class WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        clas = c.clas(
            rows[0][1],
            rows[0][2],
            rows[0][3],
            rows[0][4],
            rows[0][5],
            rows[0][0]
        )
        return clas
    return False

def get_race(value = '', param = 'id'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM race WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        race = c.race(
            rows[0][1],
            rows[0][2],
            rows[0][3],
            rows[0][4],
            rows[0][5],
            rows[0][0]
        )
        return race
    return False

def get_all_players():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM player;')
    rows = cur.fetchall()
    p = []
    t_rows = rows[0][0]

    for i in range(1, t_rows+1):
        t = get_player(i)
        p.append(t)
        
    return p

def get_all_classes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM class;')
    rows = cur.fetchall()
    c = []
    t_rows = rows[0][0]

    for i in range(1, t_rows+1):
        t = get_class(i)
        c.append(t)
        
    return c
    
def get_all_races():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM race;')
    rows = cur.fetchall()
    r = []
    t_rows = rows[0][0]

    for i in range(1, t_rows+1):
        t = get_race(i)
        r.append(t)
        
    return r
get_all_races()
def update_player(player):
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

def rm_player(player):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM player WHERE id = {player.id};")
    conn.commit()
    
def update_stats(tableName, stat, value, idName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE {tableName} SET {stat} = {value} WHERE id = {idName};")
    conn.commit()

def att_iten(player, iten):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO inventory(id_player, id_iten) VALUES("
    f"{player.id},{iten.id});")
    conn.commit()

def rm_iten(player,iten):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM inventory WHERE "
    f"id_player = {player.id} AND id_iten = {iten.id};")
    conn.commit()
    
