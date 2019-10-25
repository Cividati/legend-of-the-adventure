import database as db
import classes as c
import random as r
import time as t
import os

def default_values():

    db.create_database()
    clas =[
        c.clas('Paladin', 15, 7, 5, 5),
        c.clas('Mage', 7, 3, 10, 3),
        c.clas('Druid', 7, 7, 7, 7),
        c.clas('Warlock', 5, 2, 10, 3)
        ]
    
    for cl in clas:
        db.create_class(cl)

    race = [
        c.race('Human', 5, 5, 5, 5),
        c.race('Elf', 4, 3, 7, 6),
        c.race('Orc', 7, 8, 2, 3),
        c.race('Dwarf', 5, 9, 6, 2)
        ]

    for ra in race:
        db.create_race(ra)

    player = [
        c.player('Rubens', 1, 0, 1, 1, 10, 10, 10, 10, 10, 10),
        c.player('Tavão', 1, 0, 1, 4),
        c.player('Sader', 1, 0, 4, 2)
        ]

    for pl in player:
        db.create_player(pl)

    iten =[
        c.iten('Machado de Assis', 'Um machado feito pelos deuses da literatura brasileira', 10,10,10,10),
        c.iten('Espada de São Darwin', 'Espada feita do primeiro minério descoberto', 2, 7, 2, 4),
        c.iten('Cajado de Aristóteles', 'Cajado abençoado por Aristóteles', 0, 2, 10, 5)
        ]

    for it in iten:
        db.create_iten(it)

default_values()

def main():
    os.system('cls')
    print('Welcome to the legend of the adventure!')
    op = input('0. Exit\n1. Create character\n2. Load character\n3. Credits\nR. ')
    player = c.player('')
    os.system('cls')
    if op == '1':
        # Creating character
        
        print('\nCreating character')

        name = input('Name: ')

        totalC = db.get_all_classes()
        print()
        print('Choose your class!')
        print('id -  name  - con - str - int - spd')
        for i in totalC:
            print(i.id,'-',i.name,'-',i.con,'-',i.str,'-',i.int,'-',i.spd)

        clas_id = input('Class id: ')

        totalR = db.get_all_races()
        print('\nChoose your race!')
        print('id -  name  - con - str - int - spd')
        for i in totalR:
            print(i.id,'-',i.name,'-',i.con,'-',i.str,'-',i.int,'-',i.spd)
            
        race_id = input('\nRace id: ')

        p = c.player(name, id_class=clas_id, id_race=race_id)
        db.create_player(p)
        db.get_player(p.id)
        p.show()

        print('\nPlayer created!')

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

        print(player.name, 'selected!')
        player.show()

    elif op == '3':
        # Credits
        os.system('cls')
        print('This game is a ')
    
    else:
        print('see you next time!')
        pass


main()
