from classes.attacks.attack import Attack

class Sword(Attack):
    def __init__(self, data):
        super().__init__(data['weapon_name'], data['damage'])
    
    """
        Method for the sword's attack, takes in damage as a parameter
    """
    def swing(self, damage):
        super().basic_attack(damage)
        return damage
