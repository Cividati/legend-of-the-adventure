import random as r
import time as t

class player:

    def __init__(self, name, level = 1, exp = 0, id_class = 1, 
    id_race = 1, life = 10, mana = 10  , con = r.randint(1,10),
    Str = r.randint(1,10), Int = r.randint(1,10), 
    spd = r.randint(1,10), iD = 0):
    
        self.id = iD
        self.name  = name
        self.level = level
        self.exp = exp
        self.id_class = id_class
        self.id_race = id_race
        self.life = life
        self.mana = mana
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd

    def show(self):
        import database as db

        print('\nTake a look in your character...\n')
        print('Name:', self.name)
        print('Level:', self.level)
        print('Exp:', self.exp)
        print('Class:', db.get_class(self.id_class).name)
        print('Race:', db.get_race(self.id_race).name)
        print('Life:', self.life)
        print('Mana:', self.mana)
        print('Con:', self.con)
        print('Str:', self.str)
        print('Int:', self.int)
        print('Spd:', self.spd)

class race:

    def __init__(self, name, con = r.randint(1,10), 
    Str =  r.randint(1,10), Int =  r.randint(1,10),
    spd =  r.randint(1,10), iD = 0):
        self.id = iD
        self.name = name
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd

class clas:

    def __init__(self, name, con = r.randint(1,10), 
    Str =  r.randint(1,10), Int =  r.randint(1,10),
    spd =  r.randint(1,10), iD = 0):
        self.id = iD
        self.name = name
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd

class item:

    def __init__(self, name, description = '',
    con = r.randint(1,10), Str =  r.randint(1,10), 
    Int =  r.randint(1,10), spd =  r.randint(1,10),
    iD = 0):
        self.id = iD
        self.name = name
        self.description = description
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd
