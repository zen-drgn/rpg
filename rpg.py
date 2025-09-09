# character will be stored using a dict 
def create_character():
    chara_dict = {
        "name": "Kweli",
        "class": "Sage",
        "health": 100,
        "strength": 10,
        "luck": 0.8
    }
    return chara_dict

def print_character(character):
    print(f"Welcome to the Fantasy RPG Character Generator\nyour hero is named {character["name"]} the {character["class"]}\n") 
    print(f"Stats:\n\n- Health: {character["health"]}\n- Strength: {character["strength"]}\n- Luck: {character["luck"]}")
     
#calculate the damage a character can deal based on stats like strength and luck
def attack(character):
    base_damage = character["strength"] * 2
    if character["luck"] > 0.5:
        base_damage += 5
    line = f"{character['name']} attacks and deals {base_damage} damage!"
    return line 

#heal a character with an amount that adds to their total health 
def heal(character, amount):
    character["health"] += amount
    line = f"{character['name']} has healed by {amount} points and now has {character['health']} health"
    return line

# bellow section to run code
the_character = create_character()
#print(the_character)

print_character(the_character)

print(attack(the_character))

print(heal(the_character, 30))

print_character(the_character)


