from datetime import datetime as dt
import database as db
import classes as c
import random as r
import time as t
import os

def default_values():

    db.create_database()
    clas =[
        c.clas('Guerreiro', 7, 4, 0, 1),
        c.clas('Arqueiro', 4, 3, 0, 7),
        c.clas('Feiticeiro', 4, 2, 7, 2)
        ]
    
    for cl in clas:
        db.create_class(cl)

    race = [
        c.race('Human', 5, 5, 5, 5)
        ]

    for ra in race:
        db.create_race(ra)

    player = [
        c.player('Rubens', 1, 0, 1, 1)
        ]

    for pl in player:
        db.create_player(pl)

    iten =[
        c.item('Machado de Assis', 'Um machado feito pelos deuses da literatura brasileira', 3, 3, 0, 0),
        c.item('Espada de São Darwin', 'Espada feita do primeiro minério descoberto', 3, 3, 0, 0),
        c.item('Cajado de Flamel', 'Cajado abençoado por Aristóteles', 1, 2, 4, 0),
        c.item('Arco de Sagitário', 'Signo não influenciam, mas um disparo no peito muda o destino de alguém.', 1, 2, 0, 3),
        c.item('Crucifixo da Madeira da Cruz de Cristo', 'Adquirido em uma liquidação papal de indulgências, Lutero condena isso.', 0, 2, 4, 0)]

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
                db.delete_player(p)
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
            print('1.Floresta\n2.Deserto\n3.Caverna')

            op = input('R.')
            os.system('cls')
            if op == '1' and db.get_player_caves(player, 0) == '0':
                print('You have entered into the forest.')
                t.sleep(1.5)
                enemy1 = c.player('Mosquito', 1, 5, 1, 1, 5, 5)
                enemy2 = c.player('Cobra', 2, 10, 1, 1, 10, 15)
                enemy3 = c.player('Urso', 3, 15, 1, 1, 15, 13, 13)
                enemy4 = c.player('Leão', 4, 20, 1, 1, 20, 15, 15)
                enemy5 = c.player('Ent', 5, 40, 1, 1, 40, 17, 17, item_equipped=1)

                if player.fight(enemy1) == True:                    
                    if player.fight(enemy2) == True:
                        if player.fight(enemy3) == True:
                            if player.fight(enemy4) == True:
                                if player.fight(enemy5) == True:

                                    item = db.get_item(1)
                                    os.system('cls')
                                    print('You complete the Forest, Gratzz!')
                                    print('Here is your reward!')
                                    print(item.name+' has been added to your stash!')
                                    db.att_item(player, item)
                                    db.update_player_caves(player,0, '1')
                                    db.update_player_caves(player,1, '0')
                                    t.sleep(3.5)
            else: print('Ja terminou para você.')
                    
            if op == '2' and db.get_player_caves(player, 1) == '0':
                print('You have entered into the deserto.')
                t.sleep(1.5)
                enemy1 = c.player('Calango', 1, 5, 1, 1, 5, 5)
                enemy2 = c.player('Camelo', 2, 10, 1, 1, 10, 15)
                enemy3 = c.player('Babuíno', 3, 15, 1, 1, 15, 13, 13)
                enemy4 = c.player('Minhocão', 4, 20, 1, 1, 20, 15, 15)
                enemy5 = c.player('Escorpião Gigante', 5, 40, 1, 1, 40, 17, 17)
                enemy6 = c.player('Mumia', 6, 60, 1, 1, 60, 19, 19)
                enemy7 = c.player('Esfinge', 7, 80, 1, 1, 80, 21, 21, item_equipped=2)
                
                if player.fight(enemy1):
                    if player.fight(enemy2):
                        if player.fight(enemy3):
                            if player.fight(enemy4):
                                if player.fight(enemy5):
                                    if player.fight(enemy6):
                                        if player.fight(enemy7):

                                            item = db.get_item(3)
                                            os.system('cls')
                                            print('You complete the dungeon, Gratzz!')
                                            # colocar condição se o item já existir no inventário do jogador
                                            print('Here is your reward!')
                                            print(item.name+' has been added to your stash!')
                                            db.att_item(player, item)
                                            
                                            player.lock_level(0)
                                            t.sleep(3.5)

            elif db.get_player_caves(player, 0) == '0':
                print('Faça a floresta primeiro.')
            else: print('Já acabou para você.')

            if op == '3' and db.get_player_caves(player, 2) == '0':
                print('You have entered into the caverna.')
                t.sleep(1.5)
                enemy1 = c.player('Rato', 1, 5, 1, 1, 5, 5)
                enemy2 = c.player('Morcego', 2, 10, 1, 1, 10, 15)
                enemy3 = c.player('Goblin', 3, 15, 1, 1, 15, 13, 13)
                enemy4 = c.player('Kobold', 4, 20, 1, 1, 20, 15, 15)
                enemy5 = c.player('Esqueleto', 5, 40, 1, 1, 40, 17, 17)
                enemy6 = c.player('Orc', 6, 60, 1, 1, 60, 19, 19)
                enemy7 = c.player('Troll', 7, 80, 1, 1, 80, 21, 2, item_equipped=2)
                enemy8 = c.player('O ex da sua mãe', 8, 100, 1, 1, 100, 23, 23)
                enemy9 = c.player('Dragão', 9, 110, 1, 1, 110, 23, 23, item_equipped=3)

                if player.fight(enemy1):
                    if player.fight(enemy2):
                        if player.fight(enemy3):
                            if player.fight(enemy4):
                                if player.fight(enemy5):
                                    if player.fight(enemy6):
                                        if player.fight(enemy7):
                                            if player.fight(enemy8):
                                                if player.fight(enemy9):

                                                    item = db.get_item(3)
                                                    os.system('cls')
                                                    print('You complete the desert, Gratzz!')
                                                    print('Here is your reward!')
                                                    print(item.name+' has been added to your stash!')
                                                    db.att_item(player, item)
                                                    t.sleep(3.5)
            elif db.get_player_caves(player, 1) == '0':
                print('Faça o deserto primeiro.')
            else: print('Já acabou para você.')
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
p = db.get_player(1)
print(db.get_player_caves(p, 0))
db.update_player_caves(p, 0)
p = db.get_player(1)

print(db.get_player_caves(p, 0))