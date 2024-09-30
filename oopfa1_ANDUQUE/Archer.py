#Archer.py

from Novice import Novice
import random

class Archer(Novice):
    def __init__(self,username):
        super().__init__(username)

        self.setAgi(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp() + self.getVit())

    def rangeAttack(self,character):
        self.new_damage = self.getDamage() + random.randint(0,self.getInt())
        character.reduceHp(self.new_damage)
        print(f'{self.getUsername()} performed ranged Attack!! -{self.getDamage()} to {character.getUsername()}')


