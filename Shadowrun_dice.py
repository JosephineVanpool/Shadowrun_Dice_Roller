#!/usr/bin/env python3

#import random
from random import seed
from random import randint

global numSixes

class Shadowrun_Dice ():
    def initialRoll():
        #ask for the number of dice and set initial values
        numDice = int(input ("How many 6-sided dice do you need to roll? "))
        numSixes = 0
        initialDiceRolled = [] #inital rolling of the dice list
  
        #iterate through each die and generate an integer between 1-6 ("rolling the dice")
        #add the generated value to the list, and increment the number of sixes by 1 if the number generated is a 6
        for i in range(numDice):
            value = randint(1, 6)
            initialDiceRolled.append(value) 
            if value == 6:
                numSixes += 1
        return initialDiceRolled,numSixes


    def reRollSixes(sixes):
        rerollSixes = [] #list of 6's that were re-rolled
        numSixes=sixes
        #if there are any sixes generated during the inital roll, generate an integer between 1-6 for each 6 and decriment the number of sixes by 1
        # if there is another six that gets generated, increment the number of sixes by 1
        #loop until there are no more sixes left to generate new die for
        while numSixes != 0:
            value = randint(1, 6)
            rerollSixes.append(value) 
            numSixes -= 1
            if value == 6:
                numSixes += 1
            return rerollSixes
   


        
    diceRolled, sixes=initialRoll()
    RollSixes= reRollSixes(sixes)

    #print the results
    print (f"Results of intial throw: {diceRolled}")
    print (f"Results of re-rolling sixes: {RollSixes}")
