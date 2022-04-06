import random

class Dolphin:

    def __init__( self , name, strength, health):
        self.name = name
        self.strength = strength
        self.speed = 3
        self.health = health
        self.noise = "eee"

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        chance = random.randint(1,10)
        
        if chance > ninja.speed:
            print(f"{self.name}'s attack hit!")
            damage = random.randint(0,self.strength)
            ninja.health -= damage
            print(f"{self.name} depleted {ninja.name}'s health by {damage}!")
        
        else: print(f"{self.name} missed!")

        return self

