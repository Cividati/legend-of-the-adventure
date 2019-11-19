from datetime import datetime as dt
import database as db
import classes as c
import random as r
import time as t
import os

def default_values():

    db.create_database()
    clas =[
        c.clas('Paladin', 7, 4, 2, 2),
        c.clas('Priest', 4, 1, 5, 2),
        c.clas('Mage', 4, 1, 5, 2),
        c.clas('Druid', 4, 4, 4, 4),
        c.clas('Warlock', 2, 1, 5, 2)
        ]
    
    for cl in clas:
        db.create_class(cl)

    race = [
        c.race('Human', 5, 5, 5, 5),
        c.race('Elf', 2, 1, 4, 3),
        c.race('Orc', 3, 4, 1, 1),
        c.race('Dwarf', 2, 4, 3, 2)
        ]

    for ra in race:
        db.create_race(ra)

    player = [
        c.player('Rubens', 1, 0, 1, 1),
        c.player('Tavão', 1, 0, 1, 4),
        c.player('Sader', 1, 0, 4, 2),
        c.player('Kpis', 1, 0, 1, 1)
        ]

    for pl in player:
        db.create_player(pl)

    iten =[
        c.item('Machado de Assis', 'Um machado feito pelos deuses da literatura brasileira', 10,10,10,10),
        c.item('Espada de São Darwin', 'Espada feita do primeiro minério descoberto', 2, 7, 2, 4),
        c.item('Cajado de Aristóteles', 'Cajado abençoado por Aristóteles', 0, 2, 10, 5)
        ]

    for it in iten:
        db.create_item(it)

def main():
    os.system('cls')
    print('Welcome to the legend of the adventure!')
    op = -1
    while op != '0':
        op = input('0.Exit\n1.Create character\n2.Load character\n3.Credits\n4.Set Database\nR.')
        player = c.player('')
        os.system('cls')
        if op == '1':
            # Creating character
            
            print('Creating character')

            name = input('Name: ')

            totalC = db.get_all_classes()
            print()
            print('Choose your class!')
            print('id -  name - con - str - int - spd')
            for i in totalC:
                print(i.id,'-',i.name,'-',i.con,'-',i.str,'-',i.int,'-',i.spd)

            clas_id = input('Class id: ')
            print('You have chosen '+ db.get_class(clas_id).name)

            totalR = db.get_all_races()
            print('\nChoose your race!')
            print('id -  name - con - str - int - spd')
            for i in totalR:
                print(i.id,'-',i.name,'-',i.con,'-',i.str,'-',i.int,'-',i.spd)
                
            race_id = input('Race id: ')
            print('You have chosen '+ db.get_race(race_id).name)

            p = c.player(name, id_class=clas_id, id_race=race_id)
            db.create_player(p)
            p = db.get_player(p.name, 'name')
            p.show()
            op = input('\nAre u sure?\n1.Yes\n2.No\nR.')
            if op == '1':
                os.system('cls')
                print(p.name+' created!')
            elif op == '2':
                db.rm_player(p)
                os.system('cls')
                print('Operation aborted')

        elif op == '2':
            # Loading character
            print('loading character')
            # Creating character
            i = 0
            print('Choose yout character')
            totalP = db.get_all_players()
            for i in totalP:
                print(i.id,'-',i.name)

            op = input('Select your player id: ')
            player = db.get_player(op)
            player.show()

            op = input('\nAre u sure?\n1.Yes\n2.No\nR.')
            os.system('cls')
            if op == '1':
                print(player.name+' selected!')
                db.update_last_login(player)
                
                play(player)
            elif op == '2':
                print('Operation aborted')
            

        elif op == '3':
            # Credits
            os.system('cls')
            print('This game is made full of love ♥')
        
        elif op == '4':
            # Set default values
            print('Setting database...\nDone!')
            default_values()        

        elif op == '0':
            print('see you next time')
            pass

        else:
            print('invalid option!')

def play(player):
    os.system('cls')
    print('Here you start your adventure!')
    op = -1
    while op != '0':
        op = input('0.Exit\n1.Stash\n2.Combat\n3.View character\n4.Level up\nR.')
        os.system('cls')
        if op == '0':
            exit()
        elif op =='1':
            items = db.get_player_items(player)

            if items:
                
                print('Welcome to stash!!')
                print('This is your items:')
                for i in items:
                    print(i.id,'-',i.name)
                op = input ('Select your item to equip: ')      
                item = db.get_item(op)
                os.system('cls')
                db.equip_item(player, item)
                print(item.name+' equipped!')
                player = db.get_player(player.id)
            else:
                print('You have no items :(\nKill some mobs to get some items')
        
        elif op == '2':
            
            os.system('cls')
            print('1.Forest\n2.Dungeon\n3.Desert')
            op = input('R.')
            os.system('cls')
            if op == '1':
                print('You have entered into the forest.')
                t.sleep(1.5)
                enemy1 = c.player('Mosquito', 1, 20, 1, 1, 15, 15, 6, 4)
                enemy2 = c.player('Lion', 2, 35, 1, 1, 32, 0, 10, 10)
                enemy3 = c.player('Ent', 4, 120, 1, 1, 55, 20, 11, item_equipped=3)
                player.fight(enemy1)
                player.fight(enemy2)
                player.fight(enemy3)
            elif op == '2':
                print('You have entered into the dungeon.')
                t.sleep(1.5)
                enemy1 = c.player('Goblin', 1, 20, 1, 1, 15, 15, 6, 4)
                enemy2 = c.player('Troll', 2, 35, 1, 1, 32, 0, 10, 10)
                enemy3 = c.player('Orc Beserker', 4, 120, 1, 1, 73, 25, 13, 13, 0, 0, item_equipped=2)
                player.fight(enemy1)
                player.fight(enemy2)
                player.fight(enemy3)
            elif op == '3':
                print('You have entered into the desert.')
                t.sleep(1.5)
                enemy1 = c.player('Wasp', 1, 20, 1, 1, 15, 15, 6, 4)
                enemy2 = c.player('Skorpion', 2, 35, 1, 1, 32, 0, 10, 10)
                player.fight(enemy1)
                player.fight(enemy2)
            op = 2
        elif op == '3':
            player.show()
            print()

        elif op == '4':
            player.levelUp()

        else:
            print('invalid option')
        
main()



