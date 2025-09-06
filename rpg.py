# character will be stored using a dict 
def create_character():
    chara_dict = {
        "name": "Kweli",
        "class": "Sage",
        "health": 100,
        "strength": 77,
        "luck": 0.5
    }
    return chara_dict

def print_character(character):
    print(f"Welcome to the Fantasy RPG Character Generator\nyour hero is named {character["name"]} the {character["class"]}\n") 
    print(f"Stats:\n\n- Health: {character["health"]}\n- Strength: {character["strength"]}\n- Luck: {character["luck"]}")
     

def attack(character):
    pass

# bellow section to test run code
the_character = create_character()
#print(the_character)

print(print_character(the_character))

attack(the_character)



