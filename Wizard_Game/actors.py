import random


class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def _repr_(self):
        return "Creature:{} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12)*self.level


class Wizard(Creature):

    def attack(self, creature):
        print("The wizard {} attacks {}".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}....".format(my_roll))
        print("{} rolls {}.....".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The Wizard has handily defeated the {}".format(creature.name))
            return True
        else:
            print("The wizard has been defeated")
            return False


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2
