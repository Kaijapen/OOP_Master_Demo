"""
    # ! This class is used as a parent class for all types of attacks
    # * ==> Sets the name and damage of the weapon / spell and has a method
    # *     to print the stats of the attack.
"""
class Attack:
    # * Constructor takes 2 arguments (name and damage)
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    # * Method takes no arguments and prints the attributes for the class
    def show_stats(self):
        print(f"\n[ATTACK STATS]\nWeapon: {self.name} \nDamage: {self.damage}")
        return self
    
    def basic_attack(self, damage):
        print(f"\n[ATTACK]\nA successful attack using {self.name}")
        return damage
