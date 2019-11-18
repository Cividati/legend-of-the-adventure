import database as db
import random as r
import time as t
import os

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
        self.life = life * self.level
        self.mana = mana * self.level
        self.con = con * self.level
        self.str = Str * self.level
        self.int = Int * self.level
        self.spd = spd * self.level
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
        
        print('\nA wild '+enemy.name+' appears!')
        initial_life = self.life
        while enemy.life > 0 and self.life > 0:
             
            print()
            print(self.name+' - '+str(self.life)+' X '+str(enemy.life)+' - '+enemy.name)
            t.sleep(1)

            #player turn
            dice = r.randint(1,20)
            #print(self.name+' roll: '+str(dice))
            if dice >= enemy.con:
                totalHit = self.str + r.randint(1,4)
                print(self.name+' hit: '+str(totalHit)) 
                enemy.life -= totalHit
            else: print(self.name+' miss the attack!')
            if enemy.life <=0 : break
            #enemy turn
            dice = r.randint(1,20)
            #print(enemy.name+' roll: '+str(dice))
            if dice >= enemy.con:
                totalHit = enemy.str + r.randint(1,4)
                print(enemy.name+' hit: '+str(totalHit)) 
                self.life -= totalHit
            else: print(enemy.name+' miss the attack!')
            if self.life <0 : break

        print()
        if(self.life > 0):
            print(self.name+ ' won '+str(enemy.exp)+' exp!')    
            self.exp += enemy.exp
            self.life = initial_life

        else:
            print('You have died!')

        db.update_player(self)

    def levelUp(self):
        if self.exp >= self.level*100:
            points = int(self.exp / self.level /100)
            
            self.exp -= self.level*100
            while points > 0:
                self.level += 1
                print('You have '+str(points)+' point(s) to spend')
                points -= 1
                print('Witch skill do you want to upgrade: ')
                print('1.Con')
                print('2.Str')
                print('3.Int')
                print('4.Spd')
                op = input('R.')
                os.system('cls')
                if op == '1':
                    self.con += 1
                    print('You have added 1 point in Con!')
                    
                elif op == '2':
                    self.str += 1
                    print('You have added 1 point in Str!')
                    
                elif op == '3':
                    self.int += 1
                    print('You have added 1 point in Int!')
                    
                elif op == '4':
                    self.spd += 1
                    print('You have added 1 point in Spd!')
                print()
                db.update_player(self)
        else:
            print("You need "+str(self.level*100-self.exp)+" of exp to level up, sorry :(")

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