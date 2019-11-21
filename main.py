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
        c.player('Rubens', 1, 0, 1, 1)
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
    op = -1
    os.system('cls')
    while op != '0':
        op = input('Welcome to the legend of the adventure!\n0.Exit\n1.Create character\n2.Load character\n3.Delete Character\n4.Credits\n5.Set Database\nR.')
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
            op = '123456'
            while int(op) > len(db.get_all_players()):
                # Loading character
                os.system('cls')
                print('loading character')
                # Creating character
                print('Choose yout character')
                print('0 - EXIT')
                totalP = db.get_all_players()
                for i in totalP:
                    print(i.id,'-',i.name)

                op = input('Select your character id: ')
                os.system('cls')
                if op == '0': 
                    op = 'null'
                    break

                if db.get_player(op):

                    player = db.get_player(op)

                    player.show()

                    op = input('\nAre you sure?\n1.Yes\n2.No\nR.')
                    os.system('cls')
                    if op == '1':
                        print(player.name+' selected!')
                        db.update_last_login(player)
                        
                        play(player)
                        break
                    elif op == '2':
                        print('Operation aborted')
                        op = len(db.get_all_players()) +1
                        break

        elif op == '3':
            # Delete character
            op = '123456'
            while int(op) > len(db.get_all_players()):
                # Loading character
                os.system('cls')
                print('deleting character')
                # Deleting a character
                print('Choose yout character')
                print('0 - EXIT')
                totalP = db.get_all_players()
                for i in totalP:
                    print(i.id,'-',i.name)

                op = input('Select your character id: ')
                os.system('cls')
                if op == '0': 
                    op = 'null'
                    break

                if db.get_player(op):

                    player = db.get_player(op)
                    os.system('cls')
                    player.show()

                    op = input('\nAre you sure?\n1.Yes\n2.No\nR.')
                    if op == '1':
                        os.system('cls')
                        print(player.name+' deleted!')
                        db.delete_player(player)
                        
                        break
                    elif op == '2':
                        print('Operation aborted')
                        op = len(db.get_all_players()) +1
                        break

        elif op == '4':
            # Credits
            print('This game is made full of love ♥')
            print('Version: 0.15 Alfa')
        
        elif op == '5':
            # Set default values
            try:
                with open('database.db', 'r') as f:
                    print('Database already setted!')
                    
            except IOError:
                print('Setting database...\nDone!')
                default_values() 

        elif op == '0':
            print('see you next time')
            pass

        else:
            print('invalid option!')

def play(player):
    
    op = -1
    while op != '0':
        op = input('Here you start your adventure!\n0.Exit\n1.Stash\n2.Combat\n3.View character\n4.Level up\nR.')
        os.system('cls')
        if op == '0':
            return
        elif op =='1':
            items = db.get_player_items(player)

            if items:
                # IF player have items on statsh
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
                # Player dont have any items on stash
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

                if player.fight(enemy1) == True:                    
                    if player.fight(enemy2) == True:
                        if player.fight(enemy3) == True:

                            item = db.get_item(3)
                            os.system('cls')
                            print('You complete the Forest, Gratzz!')
                            print('Here is your reward!')
                            print(item.name+' has been added to your stash!')
                            db.att_item(player, item)
                            t.sleep(3.5)
                    
            elif op == '2':
                print('You have entered into the dungeon.')
                t.sleep(1.5)
                enemy1 = c.player('Goblin', 1, 20, 1, 1, 15, 15, 6, 4)
                enemy2 = c.player('Troll', 2, 35, 1, 1, 32, 0, 10, 10)
                enemy3 = c.player('Orc Beserker', 4, 120, 1, 1, 73, 25, 13, 13, 0, 0, item_equipped=2)
                
                if player.fight(enemy1):
                    if player.fight(enemy2):
                        if player.fight(enemy3):

                            item = db.get_item(3)
                            os.system('cls')
                            print('You complete the dungeon, Gratzz!')
                            print('Here is your reward!')
                            print(item.name+' has been added to your stash!')
                            db.att_item(player, item)
                            t.sleep(3.5)

            elif op == '3':
                print('You have entered into the desert.')
                t.sleep(1.5)
                enemy1 = c.player('Wasp', 1, 20, 1, 1, 15, 15, 6, 4)
                enemy2 = c.player('Skorpion', 2, 35, 1, 1, 32, 0, 10, 10)
                enemy3 = c.player('Sand King', 3, 135, 1, 1, 97, 0, 15, 15, item_equipped=3)

                if player.fight(enemy1):
                    if player.fight(enemy2):
                       if player.fight(enemy3):

                            item = db.get_item(3)
                            os.system('cls')
                            print('You complete the desert, Gratzz!')
                            print('Here is your reward!')
                            print(item.name+' has been added to your stash!')
                            db.att_item(player, item)
                            t.sleep(3.5)
        elif op == '3':
            # Show player ifo
            player.show()
            print()

        elif op == '4':
            # Level up!
            player.levelUp()

        else:
            print('invalid option')
        
main()
