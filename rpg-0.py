"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))
            
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

    def alive(self):
        return self.health > 0


def main():
    ShieldHero = Character("Hero",10, 5)
    Monster = Character("Goblin",6,2)

    while Monster.alive() and ShieldHero.alive():
        ShieldHero.print_status()
        Monster.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin  # Change below Step 2
            ShieldHero.attack(Monster)
            if not Monster.alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Monster.alive():
            # Goblin attacks hero # Change below Step 2
            Monster.attack(ShieldHero)
            if not ShieldHero.alive():
                print("You are dead.")

main()
