import random
# * I like to put external package imports at the top
from classes.attacks.sword import Sword
# * And imports to files I created at the bottom

class Human:
    list_humans = []

    def __init__(self, data):
        self.name = data['name']
        self.health = data['health']
        # self.defense = data['defense']
        self.weapon = Sword(data)

    """
        Stats to display the character's information
    """
    def display_info(self):
        print(f"\n[{self.name.upper()}'S STATS]\nHealth: {self.health}\nDefense: {self.defense}\n")
        self.weapon.show_stats()
        return self
    """
        Method for determining the amount of damage blocked/parried
        and IF the block/parry is successful.
    """
    def parry(self, damage):
        rand = Human.random_defense(20)
        if (rand <= self.defense):
            print(f"\n[SUCCESSFUL PARRY]\n {self.name} has successfully blocked the incomming attack!")
            damage -= self.defense
        return damage

    """
        Method for attacking an enemy
    """
    def attack(self, enemy):
        # Console output for who is attacking
        print(f"\n[{self.name.upper()} ATTACKS {enemy.name.upper()}]")
        
        # final_damage calculated by using the weapon's "swing" function & passing in and using the enemy's parry function.
        final_damage = self.weapon.swing(enemy.parry(self.weapon.damage))
        enemy.health -= final_damage # uses the final_damage 
        print(f"{enemy.name} has taken {final_damage} HP")
        return enemy

    """
        Classmethod takes in a list of dictionaries,
        and uses the dictionary data to create instances of the class.
    """

    @classmethod
    def create_many(cls, some_list):
        for character in some_list:
            human = cls(character)
            cls.list_humans.append(human)
            # human.display_info()
        return cls.list_humans
    
    @staticmethod
    def random_defense(num):
        rand = random.randint(0, num)
        return rand






# human_data = {
#     "name": "Test1",
#     "health": 150,
#     "defense": 10,
#     "weapon": Sword({"name": "Drauger Sword", "damage": 10})
# }

# human1 = Human(human_data)
# human2 = Human(human_data)

# human1.display_info().attack(human2).display_info()
