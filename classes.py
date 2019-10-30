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

        while enemy.life > 0:
            #os.system('cls')
            stat = input('Use\n1.Str\n2.Int\n3.Spd\nR.')
            if stat == '1':
                stat = self.str
            elif stat == '2':
                stat = self.int
            elif stat == '3':
                stat = self.spd
            else: stat = self.str  

            print('\nYou try to attack '+enemy.name+':'+str(enemy.life))

            dice = r.randint(1,20)
            print('You roll: '+str(dice))
            if dice >= enemy.con:
                totalHit = stat
                
                print('You hit:', (totalHit)) 
                enemy.life = enemy.life - totalHit
            else: print('You miss the attack!')
        print('You win '+str(enemy.exp)+' exp!')
        self.exp += self.exp + enemy.exp
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
