from datetime import datetime as dt
import classes as c
import sqlite3
import os

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
        # Create table item
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS item(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(45) NOT NULL,
            description VARCHAR(200) NOT NULL,
            con FLOAT NOT NULL,
            str FLOAT NOT NULL,
            int FLOAT NOT NULL,
            spd FLOAT NOT NULL  
        );
        """)
    except sqlite3.Error as e:
        print('item error:',e)

    try:
        # Create table race
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS race(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(45) NOT NULL,
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
            name VARCHAR(45) NOT NULL,
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
            name VARCHAR(45) NOT NULL,
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
            item_equipped INT DEFAULT 0,
            caves TEXT DEFAULT '0,1,1',

            FOREIGN KEY (item_equipped) REFERENCES item(id),
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
            id_item INTEGER NOT NULL,
            id_player INTEGER NOT NULL,

            FOREIGN KEY (id_item) REFERENCES item(id),
            FOREIGN KEY (id_player) REFERENCES player(id)
        );
        """)
    except sqlite3.Error as e:
        print('inventory error:',e)

    try:
        # Create table last_login
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS last_login(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER NOT NULL,
            data DATETIME NOT NULL,

            FOREIGN KEY (id_player) REFERENCES player(id)
        );
        """)
    except sqlite3.Error as e:
        print('last_login error:',e)
        
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

def create_item(item):
    conn = get_connection()

    conn.execute(f"INSERT INTO item(name, description, con, str, int, spd) VALUES( "
        f"'{item.name}', '{item.description}', '{item.con}', '{item.str}', '{item.int}', '{item.spd}');")
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

    # pegar o id do player buscando o mesmo pelo nome
    player = get_player(player.name, 'name')
    now = dt.now().strftime("%m/%d/%Y %H:%M:%S")    
    conn.execute(f"INSERT INTO last_login(id_player, data) VALUES({player.id}, '{now}')")
    conn.commit()
    conn.close()    

def get_stats(tableName, stat, idName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT {stat} FROM {tableName} WHERE id = {idName};")
    
    rows = cur.fetchall()
    value = rows[0][0]

    return value

def get_item(value = '', param = 'id'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM item WHERE {param} = "{value}";')
    
    rows = cur.fetchall()

    if rows:
        item = c.item(
            rows[0][1],
            rows[0][2],
            rows[0][3],
            rows[0][4],
            rows[0][5],
            rows[0][6],
            rows[0][0]
        )
        return item
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
            rows[0][12],
            rows[0][0],
            rows[0][13]

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
    cur.execute('SELECT * FROM player;')
    rows = cur.fetchall()
    p = []
    for i in rows:
        player = get_player(i[0])
        p.append(player)
    return p

def get_all_classes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM class;')
    rows = cur.fetchall()
    c = []
    for i in rows:
        clas = get_class(i[0])
        c.append(clas)
    return c
    
def get_all_races():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM race;')
    rows = cur.fetchall()
    r = []
    for i in rows:
        race = get_race(i[0])
        r.append(race)
    return r

def get_player_items(player):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM inventory WHERE id_player = {player.id};')
    rows = cur.fetchall()
    it = []
    for i in rows:
        item = get_item(i[1])
        it.append(item)
    return it

def get_player_caves(player, pos):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT caves FROM player WHERE id = {player.id};')
    rows = cur.fetchall()
    array = rows[0][0].split(',')
    return array[pos]

def update_player_caves(player, pos, value='1'):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT caves FROM player WHERE id = {player.id};')
    rows = cur.fetchall()
    array = rows[0][0].split(',')
    array[pos] = value
    array = ','.join(array)
    print(array)
    player.caves = array
    update_player(player)

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
                f' spd = "{player.spd}",'
                f' item_equipped = "{player.item_equipped}",'
                f' caves = "{player.caves}"'
                f' WHERE id = "{player.id}";')
    conn.commit()

def delete_player(player):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM player WHERE id = {player.id};")
    conn.commit()
    
def update_stats(tableName, stat, value, idName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE {tableName} SET {stat} = {value} WHERE id = {idName};")
    conn.commit()

def update_last_login(player):
    conn = get_connection()
    cur = conn.cursor()
    now = dt.now().strftime("%m/%d/%Y %H:%M:%S") 
    cur.execute(f"UPDATE last_login SET data = '{now}' WHERE id_player = {player.id};")
    conn.commit()

def att_item(player, item):
    # attribute a item to a player
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO inventory(id_player, id_item) VALUES("
    f"{player.id},{item.id});")
    conn.commit()

def rm_item(player, item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM inventory WHERE "
    f"id_player = {player.id} AND id_item = {item.id};")
    conn.commit()

def search_item(player, item):
    conn = get_connection()
    cur = conn.cursor()
    print('player: ', player.id)
    print('item: ', item.id)
    cur.execute(f"SELECT * FROM inventory WHERE "
    f"id_player = {player.id} AND id_item = {item.id};")
    rows = cur.fetchall()
    print(rows)
    it = []
    for i in rows:
        print(i)
        item = get_item(i[1])
        it.append(item)
    return it

def equip_item(player, item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE player SET item_equipped = {item.id} WHERE id = {player.id};")
    conn.commit()