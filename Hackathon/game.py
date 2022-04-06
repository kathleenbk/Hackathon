from classes.ninja import Ninja
from classes.dolphin import Dolphin

mike = Ninja("Mike")

gerald = Dolphin("Gerald", 8, 100)
timothy = Dolphin("Timothy", 4, 40)

finn = Dolphin("Finn", 30, 150)


def battle(ninja, dolphin):
    # print("Battling!")
    dolphin.show_stats()
    ninja.show_stats()
    while dolphin.health > 0 and ninja.health  > 0 :
        print(f"{ninja.name} is attacking {dolphin.name}!")
        ninja.attack(dolphin)
        print(f"{dolphin.name}'s Health: {dolphin.health}")
        if dolphin.health > 0:
            print(f"{dolphin.name} is attacking {ninja.name}!")
            dolphin.attack(ninja)
            print(f"{ninja.name}'s Health: {ninja.health}")
    
    if dolphin.health>ninja.health:
        dolphin.show_stats()
        print(f"{dolphin.name} wins!")
        
    else: 
        ninja.show_stats()
        print(f"{ninja.name} wins!")
        

battle(mike, timothy)
battle(mike, gerald)
battle(mike, finn)

