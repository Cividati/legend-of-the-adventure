import database as db
import classes as c
import random as r

def main():

    #db.create_database()

    class1 = c.clas(1, 'Paladin', 15, 7, 5, 5)
    class2 = c.clas(2, 'Mage', 7, 3, 10, 3)
    class3 = c.clas(3, 'Druid', 7, 7, 7, 7)
    
    db.create_class(class1)
    db.create_class(class2)
    db.create_class(class3)

    race1 = c.race(1, 'Human', 5, 5, 5, 5)
    race2 = c.race(2, 'Elf', 4, 3, 7, 6)
    race3 = c.race(3, 'Orc', 7, 8, 2, 3)
    race4 = c.race(4, 'Dwarf', 5, 9, 6, 2)

    player1 = c.player(1, 'Rubens', 1, 0, 1, 1, 10, 10, 10, 10, 10, 10)
    player2 = c.player(2, 'Tavão', 1, 0, 1, 4)


    #db.create_player(player1)
main()
