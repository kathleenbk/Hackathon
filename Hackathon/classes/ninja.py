import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , dolphin ):
        chance = random.randint(1,10)

        if chance > dolphin.speed:
            print(f"{self.name}'s attack hit!")
            damage = random.randint(5,self.strength)
            dolphin.health -= damage
            print(f"{self.name} depleted {dolphin.name}'s health by {damage}!")
        
        else: print(f"{self.name} missed!")

        return self