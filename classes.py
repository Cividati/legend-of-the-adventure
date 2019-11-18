import random as r
import time as t

class player:

    def __init__(self, name, level = 1, exp = 0, id_class = 1, 
    id_race = 1, life = 10, mana = 10  , con = r.randint(1,10),
    Str = r.randint(1,10), Int = r.randint(1,10), 
    spd = r.randint(1,10), item_equipped = 0, iD = 0):
    
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
        self.item_equipped = item_equipped

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

    def fight(self, enemy):
        import os
        import database as db
        print('\nA wild '+enemy.name+' appears!')
        initial_life = self.life
        while enemy.life > 0 or self.life > 0:
             
            print()
            print(self.name+'-'+str(self.life)+' X '+str(enemy.life)+'-'+enemy.name)
            t.sleep(1)

            #player turn
            dice = r.randint(1,20)
            print(self.name+' roll: '+str(dice))
            if dice >= enemy.con:
                totalHit = self.str + r.randint(1,4)
                print(self.name+' hit:'+str(totalHit)) 
                enemy.life -= totalHit
            else: print(self.name+' miss the attack!')

            #enemy turn
            dice = r.randint(1,20)
            print(enemy.name+' roll: '+str(dice))
            if dice >= enemy.con:
                totalHit = enemy.str + r.randint(1,4)
                print(enemy.name+' hit:'+str(totalHit)) 
                self.life -= totalHit
            else: print(enemy.name+' miss the attack!')

        print()
        print('You win '+str(enemy.exp)+' exp!')
        self.exp += enemy.exp
        self.life = initial_life

        db.update_player(self)

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