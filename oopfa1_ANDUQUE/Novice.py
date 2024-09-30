#Novice.py

from Character import Character

class Novice(Character):

    def __init__(self,username):
        super().__init__(username)
        self.setStr(20)
    def basicAttack(self,charater):
        charater.reduceHp(self.getDamage() + self.getStr())

        print(f'{self.getUsername()} performed Basic Attack! -{self.getDamage()}hp to {charater.getUsername()}')






