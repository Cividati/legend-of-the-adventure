import database as db
import classes as c
import random as r
import time as t

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
