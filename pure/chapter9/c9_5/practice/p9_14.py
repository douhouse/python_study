from random import randint

class Die():

    def __init__(self, sides=6):
        '''创建一个骰子，默认点数为6'''
        self.sides = sides


    def roll_die(self):
        '''roll骰子，点数在1～6中随机'''
        point = randint(1, self.sides)
        print("The point is: " + str(point))

my_die = Die(20)

for i in range(10):
    my_die.roll_die()
