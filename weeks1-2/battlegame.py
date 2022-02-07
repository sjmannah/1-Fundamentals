wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_daamge = 20

dragon_hp = 300
dragon_damage = 50
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_daamge
        break
    else: 
        print("Unknown Character")
print("Your Character is:", character, "\nYour Hp:", my_hp, "\nYour Damage:", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!\nThe Dragon now has", dragon_hp, "Hp\n")
    if dragon_hp <= 0:
        print("The dragon has lost the battle!")
        break
    my_hp = my_hp - dragon_damage
    print("The dragon damaged the", character, "\nThe", character, " now has", my_hp, "HP\n")
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break