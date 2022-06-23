from random import randint
from time import sleep as wait

class Dice():
    def __init__(self):
        self.results=[]
    def roll(self):
        x= randint(1,6)
        self.results.append(x)
        return(x)
    def results(self,roll):
        return self.results.add(roll)
    def showResults(self):
        return self.results

Dicee = Dice()
print("Hello in Dice Roll Simulator!")
while True:
    wait(1)
    y=input("Do u wanna role a dice? (y/n): ")
    if y == "y":
        res = Dicee.roll()
        print("You roll was: ", res)
        print("Your overall results are: ",Dicee.showResults(),"\n")
        continue
    elif y == "n":
        print("Bye!")
        wait(1)
        break
    else:
        print("Please ansewr y/n\n")
        continue

        

