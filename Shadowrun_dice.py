from random import seed
from random import randint

numDice = int(input ("How many 6-sided dice do you need to roll? "))
diceRolled = []
numSixes = 0
rerollSixes = []
# seed random number generator
seed()


for i in range(numDice):
    value = randint(1, 6)
    diceRolled.append(value) 
    if value == 6:
        numSixes += 1
    
while 
print(f"Results of intial throw: {diceRolled}")
print (f"Number of sixes: {numSixes}")