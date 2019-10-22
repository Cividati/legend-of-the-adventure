import struct as stc
import database as db
import classes as c
import random as r
import time as t

def main():

    db.create_database()
    clas =[
        c.clas(1, 'Paladin', 15, 7, 5, 5),
        c.clas(2, 'Mage', 7, 3, 10, 3),
        c.clas(3, 'Druid', 7, 7, 7, 7),
        c.clas(4, 'Warlock', 5, 2, 10, 3)]
    
    for cl in clas:
        db.create_class(cl)

    race = [
        c.race(1, 'Human', 5, 5, 5, 5),
        c.race(2, 'Elf', 4, 3, 7, 6),
        c.race(3, 'Orc', 7, 8, 2, 3),
        c.race(4, 'Dwarf', 5, 9, 6, 2)]

    for ra in race:
        db.create_race(ra)

    player = [
        c.player(1, 'Rubens', 1, 0, 1, 1, 10, 10, 10, 10, 10, 10),
        c.player(2, 'Tavão', 1, 0, 1, 4),
        c.player(3, 'Sader', 1, 0, 4, 2)]

    for pl in player:
        db.create_player(pl)

main()
