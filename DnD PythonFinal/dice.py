import random as r  # use the ranom for getting 1-6
import mainMenu

def diceRoll():     #naming the function, propper
    
    roll1 = 0       #storage for my rolls
    roll2 = 0
    roll3 = 0
    roll4 = 0
    rollList = []   #add to list to make finding the smallest roll
    lowestRoll = 0

    roll1 = r.randint(1,6) #"roll" to get a number between 1 and 6
    rollList += str(roll1) # add the roll to the list
    roll2 = r.randint(1,6)
    rollList += str(roll2)
    roll3 = r.randint(1,6)
    rollList += str(roll3)
    roll4 = r.randint(1,6)
    rollList += str(roll4)
    
    lowestRoll = min(rollList) # find the lowest roll
    scoreRoll = roll1+roll2+roll3+roll4-int(lowestRoll) # add each roll together
                                                # minus the lowest roll to get score
                
    return(scoreRoll)   # return the score to character score for use


diceRoll()
    # commented out so i can test solo if i need to


def replacementDice():
    rollAgain = True
    check = ""
    print("let's roll some dice!")
    while rollAgain == True:
        d = input("Which die would you like to roll?\n <d100>, <d20>, <d12>, <d10>, <d8>, <d6>, <d4>")
        # mult = int(input("How many of that die would you like to roll?"))
        if d == "d100":
            roll = str(r.randint(1,100))
            if roll == "69":        # a bit of fun
                       print("\nYou rolled: 69.\n Nice.")
            else:
                print("\nYou rolled: "+ roll)

        elif d == "d20":            # each of these different "dice" are basically the same
            roll = str(r.randint(1,20))
            if roll == "20":
                print("\nYou rolled a natty 20 my dude!")
            else:
                print("\nYou rolled a: "+roll)
        elif d == "d12":            # check which "die" user wants to roll
            roll = str(r.randint(1,12)) # use rand int to "roll" the die
            print("\nYou rolled: " + roll)  # print result
        elif d == "d10":
            roll = str(r.randint(1,10))
            print("\nYou rolled: " + roll)
        elif d == "d8":
            roll = str(r.randint(1,8))
            print("\nYou rolled: " + roll)
        elif d == "d6":
            roll = str(r.randint(1,6))
            print("\nYou rolled: " + roll)
        elif d == "d4":
            roll = str(r.randint(1,4))
            print("\nYou rolled: " + roll)
        else:                       # easy check if user entered what i want
            print("\nTry entering one of the options")

        check = input("Would you like to roll some more?\n <y> or <n>")
        if check == "n" or check == "no":   # a little loop to give the option to stay in this function
            rollAgain = False
            #home = mainMenu.mainMenu()

#replacementDice()
    
        
              


        
        

        
