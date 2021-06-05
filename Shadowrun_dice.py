#!/usr/bin/env python3

from random import randint

class Shadowrun_Dice ():
    def initialRoll():
        #ask for the number of dice and set initial values
        numDice = int(input ("How many 6-sided dice do you need to roll? "))
        numSixes = 0
        initialDiceRolled = [] #inital list for rolling of the dice
  
        #iterate through each die and generate an integer between 1-6 ("rolling the dice")
        #add the generated value to the list, and increment the number of sixes by 1 if the number generated is a 6
        for i in range(numDice):
            value = randint(1, 6)
            initialDiceRolled.append(value) 
            if value == 6:
                numSixes += 1
        return initialDiceRolled,numSixes


    def RollSixes(sixes):
        numSixes=sixes
        rerollSixes = [] #empty list of 6's that were re-rolled

        #if sixes are generated during the inital roll, generate an integer between 1-6 for each 6 and decriment the number of sixes by 1
        # if there is a six that gets generated, increment the number of sixes by 1, and continue until no more sixes
        while numSixes != 0:
            value = randint(1, 6)
            rerollSixes.append(value) 
            numSixes -= 1
            if value == 6:
                numSixes += 1
        return rerollSixes
           
    diceRolled, numSixes=initialRoll()
    reRollSixes= RollSixes(numSixes)

    #print the results
    print (f"Results of intial throw: {diceRolled}")
    print (f"Results of re-rolling sixes: {reRollSixes}")
