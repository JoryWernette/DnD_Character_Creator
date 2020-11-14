import characterCreation as cc          # setup for option 1, create
import viewCharacter as vc  # setup for option 2, viewing created characters
import openHandbook as oh   # setup for option3, viewing the player handbook
import dice as roll     # setup for option 4, die roller


# main menu

def mainMenu():
    stop = "no"             # storage for the menu loop
    
    print("\n\n\n\n\n")     # create space for looks
    print("============================")
    print("This is my D&D character creation program.")
    print("Where shall we begin?\n\n")
    

    while stop == "no":     # begin loop
        print("1) Create a Character (create)\n2) View a Character   (view)\n3) Player Handbook    (handbook)\n4) Roll Dice          (roll dice)\n5)\t (Quit)\n")
        mainMenuChoice = input("Choose your path: ")    # main display of options
        mainMenuChoice.lower()
        if mainMenuChoice == "create" or mainMenuChoice == "1":
            characterCreation = cc.characterScores() # begin character creation process
            
        elif mainMenuChoice == "view" or mainMenuChoice == "2":
            viewCharacter = vc.view()       # begins options for viewing a character
            
        elif mainMenuChoice == "handbook" or mainMenuChoice == "3":     
            openHandbook = oh.handbook()    # pulls up handbook pdf in browser window

        elif mainMenuChoice == "roll dice" or mainMenuChoice == "rolldice" or mainMenuChoice == "4":
            rollDice = roll.replacementDice() # fires up the dice rolling function
            
        elif mainMenuChoice == "quit" or mainMenuChoice == "5":
            print("Until next time, farewell.")
            stop = "yes"                    # quits program
            break
            
        else:
            print("Try something else, my dude!")
            print("============================")
            print("\n\n\n\n\n")             # create space
            print("============================")
    
    
mainMenu()
