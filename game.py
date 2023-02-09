from classes.characters.human import Human
from classes.attacks.sword import Sword

# ! ^^ Per best practice, imports always go at the top of the file,
'''
    # ! If you have a long description of the contents of your code, put it after the imports.
    # TODO: Overall goal:
    # ==> Pass a dictionary into the constructor instead of individual inputs
    # * ==> Player can customize their character based on console inputs
    # * ==> Player can fight with pre-made characters
    # ! Goal: Learn more about OOP and how we can use user submitted data with our classes
'''
human_data = {
        "name": "Paladin Mike",
        "health": 400,
        "defense": 30,
        "weapon_name": "Buster Sword",
        "damage": 30
    }

human1 = Human(human_data)
human1.display_info()
# human = Human.create_many(humans_data)
# print(f"[LIST OF DICTIONARIES]\n{humans_data}")
# print(F"[LIST OF HUMAN OBJECTS]\n{human}")

# # print(humans_data[0]['name'])
# print(human[0].name)
