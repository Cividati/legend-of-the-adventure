import database as db
import random as r
import time as t
import os

class player:

    def __init__(self, name, level = 1, exp = 0, id_class = 1, 
    id_race = 1, life = 10, mana = 10, con = r.randint(1,10),
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

        print('Take a look in your character...\n')
        print('Name:', self.name)
        print('Level:', self.level)
        print('Exp:', self.exp)
        print('Class:', db.get_class(self.id_class).name)
        print('Race:', db.get_race(self.id_race).name)
        print('Life:', self.life,'+ (',db.get_item(self.item_equipped).con/2 if self.item_equipped!=0 else '0', ')')
        print('Mana:', self.mana,'+ (',db.get_item(self.item_equipped).int/2 if self.item_equipped!=0 else '0', ')')
        print('Con:', self.con,'+ (',db.get_item(self.item_equipped).con if self.item_equipped!=0 else '0', ')')
        print('Str:', self.str,'+ (',db.get_item(self.item_equipped).str if self.item_equipped!=0 else '0', ')')
        print('Int:', self.int,'+ (',db.get_item(self.item_equipped).int if self.item_equipped!=0 else '0', ')')
        print('Spd:', self.spd,'+ (',db.get_item(self.item_equipped).spd if self.item_equipped!=0 else '0', ')')
        print('Item:', db.get_item(self.item_equipped).name if self.item_equipped!=0 else 'none')

    def fight(self, enemy):
        
        player = self
        initial_life = self.life
        round = 0
        while enemy.life > 0 and player.life > 0:
             
            os.system('cls')
            round +=1
            print('Round: '+str(round))
            print(player.name+' - '+str(player.life)+' X '+str(enemy.life)+' - '+enemy.name)
            t.sleep(1)

            #player turn
            dice = r.randint(1,20)
            #print(player.name+' roll: '+str(dice))
            if dice + player.str/5 >= enemy.con + db.get_item(enemy.item_equipped).con if enemy.item_equipped!=0 else enemy.con:
                totalHit = player.str + r.randint(1,4) + db.get_item(player.item_equipped).str if player.item_equipped!=0 else player.str + r.randint(1,4)
                print(player.name+' hit: '+str(totalHit)) 
                enemy.life -= totalHit
            else: print(player.name+' miss the attack!')
            t.sleep(1)
            if enemy.life <=0 : break
            #enemy turn
            dice = r.randint(1,20)
            #print(enemy.name+' roll: '+str(dice))
            if dice + enemy.str/5 >= player.con + db.get_item(player.item_equipped).con if player.item_equipped!=0 else player.con:
                totalHit = enemy.str + r.randint(1,4) + db.get_item(enemy.item_equipped).str if enemy.item_equipped!=0 else enemy.str + r.randint(1,4)
                print(enemy.name+' hit: '+str(totalHit)) 
                player.life -= totalHit
            else: print(enemy.name+' miss the attack!')
            if player.life <= 0 : break
            t.sleep(1.5)

        print()
        if(player.life > 0):
            # you win
            print(player.name+ ' have defeated '+enemy.name)
            print('You got '+str(enemy.exp)+' exp!')    
            self.exp += enemy.exp
            if(enemy.item_equipped != 0):
                item = db.get_item(enemy.item_equipped)
                db.att_item(self, item)
                print('You drop the '+item.name)
            self.life = initial_life
            db.update_player(self)
            t.sleep(3)
            return True
        
        else:
            print(enemy.name+' have killed you!')
            self.life = initial_life
            t.sleep(3)
            return False

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
                    self.life +=2
                    
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
            print("You don't have amount of exp to level up")
            print("You need more "+str(self.level*100-self.exp)+" of exp to level up")
            print("sorry :(")

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