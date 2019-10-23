import database as db
import classes as c
import random as r
import time as t

def default_values():

    db.create_database()
    clas =[
        c.clas(1, 'Paladin', 15, 7, 5, 5),
        c.clas(2, 'Mage', 7, 3, 10, 3),
        c.clas(3, 'Druid', 7, 7, 7, 7),
        c.clas(4, 'Warlock', 5, 2, 10, 3)
        ]
    
    for cl in clas:
        db.create_class(cl)

    race = [
        c.race(1, 'Human', 5, 5, 5, 5),
        c.race(2, 'Elf', 4, 3, 7, 6),
        c.race(3, 'Orc', 7, 8, 2, 3),
        c.race(4, 'Dwarf', 5, 9, 6, 2)
        ]

    for ra in race:
        db.create_race(ra)

    player = [
        c.player(1, 'Rubens', 1, 0, 1, 1, 10, 10, 10, 10, 10, 10),
        c.player(2, 'Tavão', 1, 0, 1, 4),
        c.player(3, 'Sader', 1, 0, 4, 2),
        c.player(4, 'Kpis', 1, 0, 1, 1)
        ]

    for pl in player:
        db.create_player(pl)

    iten =[
        c.iten(1, 'Machado de Assis', 'Um machado feito pelos deuses da literatura brasileira', 10,10,10,10),
        c.iten(2, 'Espada de São Darwin', 'Espada feita do primeiro minério descoberto', 0, 7, 2, 4),
        c.iten(3, 'Cajado de Aristóteles', 'Cajado abençoado por Aristóteles', 0, 2, 10, 5)
        ]

    for it in iten:
        db.create_iten(it)

default_values()
