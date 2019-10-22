import random as r

class player:

    def __init__(self, iD, name, level, exp, id_class, id_race, life = 10, mana = 10  , con = r.randint(1,10), Str = r.randint(1,10), Int = r.randint(1,10), spd = r.randint(1,10)):
    
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

class race:

    def __init__(self, iD, name, con, Str, Int, spd):
        self.id = iD
        self.name = name
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd

class clas:

    def __init__(self, iD, name, con, Str, Int, spd):
        self.id = iD
        self.name = name
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd

class iten:

    def __init__(self, iD, name, description, con, Str, Int, spd):
        self.id = iD
        self.name = name
        self.description = description
        self.con = con
        self.str = Str
        self.int = Int
        self.spd = spd
