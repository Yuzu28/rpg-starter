import random


class Character():
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def attack(self, enemy):
        if not self.alive():
            return
        print ("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)

    def receive_damage(self, points):
        self.health -= points
        print ("%s received %d damage." % (self.name, points))
        if self.name == 'Zombie' and self.health <= -10:
            print ("%s is dead." % self.name)
        elif self.name != 'Zombie' and self.health <= 0:
            print ("%s is dead." % self.name)

    def print_status(self):
        print ("%s has %d health and %d power." % (self.name, self.health, self.power))

    def alive(self):
        return self.health > 0


class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        if not self.alive():
            return
        print ("%s attacks %s" % (self.name, enemy.name))
        double_power = random.random() > 0.8
        if double_power == True:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
      

    def restore(self):
        self.health = 10
        print ("Hero's heath is restored to %d!" % self.health)
    
    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    
       
class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2
        self.coins = 10
    

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 10
        self.power = 3
        self.coins = 8

    def receive_damage(self, points):
        self.health -= points
        # recuperate 2 health points after being attacked with a probability of 20%
        Recuperate = random.random() > 0.8
        if Recuperate == True:
            self.health += 2
        print ("The %s received %d damage." % (self.name, points))
        if self.health <= 0:
            print ("The %s is DEAD." % self.name)

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 5
        self.coins = 7
    
    def receive_damage(self, points):
        # take damage about once out of every ten times he is attacked.
        shadow_damage = random.random() > 0.9
        if shadow_damage == True:
            self.health -= points
            print ("The %s received %d damage." % (self.name, points))
        else:
            print ("The %s received no damage." % (self.name))
        if self.health <= 0:
            print ("%s is DEAD." % self.name)

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 6
        self.power = 2
        self.coins = 13
    
    def alive(self):
        return self.health > -10





class RandomBadGuy(Character):
    def __init__(self):
        self.name = 'RandomBadGuy'
        self.health = 5
        self.power = 5
        self.coins = 7

    def attack(self, enemy):
        if not self.alive():
            return
        print ("%s attacks %s" % (self.name, enemy.name))
        RandomBadGuy_damage = random.random() > 0.4
        if RandomBadGuy_damage == True:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)

class Elves(Character):
    def __init__(self):
        self.name = 'Elves'
        self.health = 3
        self.power = 3
        self.coins = 9

    def attack(self, enemy):
        if not self.alive():
            return
        print ("%s attacks %s" % (self.name, enemy.name))
        Elves_damage = random.random() > 0.6
        if Elves_damage == True:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)


class Battle(object):
    def fight(self, hero, enemy):
        print("=====================")
        print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False



class Evade(object):
    cost = 5
    name = 'Evade'
    def apply(self, character):
        character.evade += 2
        print ("%s's evade amount increased to %d." % (character.name, character.evade))

class Armor(object):
    cost = 4
    name = "Armour"
    def apply(self, character):
        character.armor += 2
        print ("The %s's armor increased to %d." % (character.name, character.armor))

class HealthPack(object):
    cost = 5
    name = 'HealthPack'
    def apply(self, character):
        character.health += 10
        print ("The %s's health increased to %d." % (character.name, character.health))

class Tonic(object):
    cost = 5
    name = 'Tonic'
    def apply(self, character):
        character.health -= 4
        print ("The %s's health increased to %d." % (character.name, character.health))

class Kunai(object):
    cost = 6
    name = 'Kunai'
    def apply(self, character):
        character.power += 15
        print ("The %s's power increased to %d." % (character.name, character.power))





class Store(object):
    items = [Tonic, Kunai, HealthPack, Armor, Evade]
    def Do_shopping(self, hero):
        while True:
            print("✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸")
            print("     Welcome to the store!")
            print("✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸✸")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)


hero = Hero() 
enemies = [ Elves(), Zombie(), Goblin(), RandomBadGuy(), Medic(), Shadow() ]
Battle_Start = Battle()
Shopping_Store = Store()

for enemy in enemies:
    hero_won = Battle_Start.fight(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    Shopping_Store.Do_shopping(hero)

print("YOU WIN!")