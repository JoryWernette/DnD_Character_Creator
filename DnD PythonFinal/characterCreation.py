import time                 #this is a cheeky thing i found to make my output cooler
import dice as roll     #my dicerolling function
import webbrowser as wb     #this is for future use if user has questions about the races or classes


def characterScores():

                        #storage
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    reroll = 0          #house rule check
    scoreRoll = 0       #temp variable for the die roll
    characterName = ""
    happy = "no"        #loop control
    check = ""
    abilityScores = []  #considered adding to a list, but probably wont follow through
                        #making space
    print("============================")
    print("\n\n\n\n\n")
    print("============================")
                        #loop controls naming portion
    while happy == "no":
        characterName = input(str("Firstly, what would you like your character to be named?"))              #get input for the name
        print("Are you happy with your character being called: "+characterName+"?")                         #display name and ask if it is okay
        check = input("If "+characterName+" is not correct, enter 'no' otherwise hit <enter> to continue")  #is the check to see if we can continue
        if check == "no" or check == "'no'":
            happy = "no"                        #a simple gateway to check if the input is what I expect
        else:
            happy = "yes"
    print("We will now roll for your base skills:\nStrength,\nDexterity,\nConstitution,\nIntelligence,\nWisdom,\nand Charisma")
    time.sleep(3)                               #these give user some time to read my outputs 
    print("There are choices later on that may adjust these scores.")
    time.sleep(2)
    print("We will decide these scores by 'rolling' 4 six sided dice. We will then drop the lowest die.")
    time.sleep(3)
    print("Essentially this gives you a score between 3 and 18.")
    time.sleep(2)
    print("If a result is less than 10, then, per house rules, we can re-roll it, but only once in this creation process.")
    time.sleep(3)
    print("Once we have 6 scores, we will move on to choosing the race and class for "+characterName+".")
    time.sleep(2)
    
    print("Lets roll for our scores: ")
    time.sleep(1)
    
                                            #these blocks are all identical
    strength = roll.diceRoll()              #use dice rolling function to get a number 
    print("Strength = ", str(strength))     #display that number as the ability score
    time.sleep(1)                           #pause for coolness
    if strength < 10:                       #check if house rules apply to re-roll
        decision = input("Would you like to roll for strength again?\n<y> or <n>")  #ask user if they'd like to (as can only be done once)
        if decision == 'y':                 #the loop controlling the input
            strength = roll.diceRoll()      #reroll
            print("Strength = ", str(strength)) #display score
            abilityScores += str(strength)  #add to list for later, won't actually use this, but just in case
            reroll += 1                     #add to reroll counter to make sure user can't use reroll feature more than once
    else:
        abilityScores += str(strength)      #if they didnt reroll this adds original roll to the list
        
    dexterity = roll.diceRoll()
    print("Dexterity = ", str(dexterity))   #basically the same as the above block, except its for dex
    time.sleep(1)
    if dexterity < 10 and reroll!= 1:       #this line is really the only different one, it checks if user used up the reroll
        decision = input("Would you like to roll for dexterity again?\n<y> or <n>")
        if decision == 'y':
            dexterity = roll.diceRoll()
            print("Dexterity = ", str(dexterity))
            abilityScores += str(dexterity)
            reroll += 1
    else:
        abilityScores += str(dexterity)
            
    constitution = roll.diceRoll()
    time.sleep(1)                           #the same block, but for con
    print("Constitution = ", str(constitution)) 
    if constitution < 10 and reroll!= 1:
        decision = input("Would you like to roll for constitution again?\n<y> or <n>")
        if decision == 'y':
            constitution = roll.diceRoll()
            print("Constitution = ", str(constitution))
            abilityScores += str(constitution)
            reroll += 1
    else:
        abilityScores += str(constitution)
    
    intelligence = roll.diceRoll()      #same again
    print("Intelligence = ", str(intelligence))
    time.sleep(1)
    if intelligence < 10 and reroll!= 1:
        decision = input("Would you like to roll for intelligence again?\n<y> or <n>")
        if decision == 'y':
            intelligence = roll.diceRoll()
            print("Intelligence = ", str(intelligence))
            abilityScores += str(intelligence)
            reroll += 1
    else:
        abilityScores += str(intelligence)
    
    wisdom = roll.diceRoll()
    print("Wisdom = ", str(wisdom))     # same
    time.sleep(1)
    if wisdom < 10 and reroll!= 1:
        decision = input("Would you like to roll for wisdom again?\n<y> or <n>")
        if decision == 'y':
            wisdom = roll.diceRoll()
            print("Wisdom = ", str(wisdom))
            abilityScores += str(wisdom)
            reroll += 1
    else:
        abilityScores += str(wisdom)
    
    charisma = roll.diceRoll()
    print("Charisma = ", str(charisma))#ditto
    time.sleep(1)
    if charisma < 10 and reroll!= 1:
        decision = input("Would you like to roll for charisma again?\n<y> or <n>")
        if decision == 'y':
            charisma = roll.diceRoll()
            print("Charisma = ", str(charisma))
            abilityScores += str(charisma)
            reroll += 1
    else:
        abilityScores += str(charisma)

    print("============================")
    print("\n\n\n\n\n")                     #making space for style
    print("============================")
    print("Very good!\nYour ability scores for "+characterName+" are:")
    print("\nStrength: "+str(strength))     #display what we just rolled, but together
    print("\nDexterity: "+ str(dexterity))
    print("\nConstitution: "+ str(constitution))
    print("\nIntelligence: "+ str(intelligence))
    print("\nWisdom: "+ str(wisdom))
    print("\nCharisma: "+ str(charisma))

    time.sleep(1)



#def characterRace():



    raceChosen = False      #storage for the character race function
    choice = ""
    characterRace = ""      # for ease i took out the def characterRace(): to make it all in one file because it took out a step, but ill treat it the same
    decided = "no"
    decideAgain = "no"

    print("Now we are going to pick a Race.")
    time.sleep(1)           # short introduction to the user 
    
    while raceChosen == False:
        print("These are the races you have to choose from: ")
        time.sleep(1)       # list options with cool pause
        print("Dragonborn <dragonborn>")
        print("Dwarf <dwarf>")
        print("Elf <elf>")
        print("Gnome <gnome>")
        print("Half-Elf <half-elf")
        print("Halfling <halfling>")
        print("Half-Orc <half-orc>")
        print("Human <human>")
        print("Tiefling <tiefling>")
        time.sleep(1)
        print("If you'd like more information about something, add 'q' behind it.")
        time.sleep(1)
        print("That would look something like\nraceq")
        time.sleep(1)

        choice = input("Enter your choice now: ")   #get choice from user
        choice = choice.strip() # make sure Caps dont matter and if a space is pressed before answering it goes away
        choice = choice.lower()

        if choice == "dragonborn": #if choice is dragonborn
            characterRace = choice #hold onto that choice in an easier to remember variable
            print("As a Dragonborn, "+ characterName + " gets a +2 to Strength and +1 to Charisma.") #describe bonuses
            strength += 2   #implement bonuses
            charisma += 1
            raceChosen = True #end loop
        elif choice == "dragonbornq": # if user has a question on the race
            wb.open_new_tab("https://www.dndbeyond.com/races/dragonborn") # open new tab to dnd beyond at the dragon born page

        elif choice == "dwarf":
            characterRace = choice # each of these blocks are basically the same too
            print("As a Dwarf, "+ characterName + " gets a +2 to Constitution.") # except for this block, since the bonuses are different between classes
            constitution += 2
            raceChosen = True
        elif choice == "dwarfq":
            wb.open_new_tab("https://www.dndbeyond.com/races/dwarf")

        elif choice == "elf":
            characterRace = choice
            print("As an Elf, "+ characterName + " gets a +2 to Dexterity.")
            dexterity += 2
            raceChosen == True
            break
        elif choice == "elfq":
            wb.open_new_tab("https://www.dndbeyond.com/races/elf")

        elif choice == "gnome":
            characterRace = choice
            print("As a Gnome, "+ characterName + " gets a +2 to Intelligence.")
            intelligence += 2
            raceChosen = True
        elif choice == "gnomeq":
            wb.open_new_tab("https://www.dndbeyond.com/races/gnome")

        elif choice == "half-elf":
            characterRace = choice # but the extra bonuses get weird here, because the user gets to add +1 to 2 different ability scores
            print("As a Half-Elf, "+ characterName + " gets a +2 to Charisma.")
            charisma += 2
            print(characterName + " also gets a +1 to two other ability scores.")
            print("The ability score options are: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.") #list options
            
            while decided == "no":  #so i made 2 similar loops to make user decide which scores to add to
                halfelfPlus = input("Enter the name of the first of two scores you'd like to increase: ") #get decision
                if halfelfPlus == "strength": # if its this ability score
                    strength += 1 # add 1 to the score
                    decided = "yes" # end the loop
                elif halfelfPlus == "dexterity":
                    dexterity += 1
                    decided = "yes"
                elif halfelfPlus == "constitution":
                    constitution += 1
                    decided = "yes"
                elif halfelfPlus == "intelligence":
                    intelligence += 1
                    decided = "yes"
                elif halfelfPlus == "wisdom":
                    wisdom += 1
                    decided = "yes"
                elif halfelfPlus == "charisma":
                    charisma += 1
                    decided = "yes"
                else:       # if you enter something i do not like, try again
                    print("try again")

            while decideAgain == "no":   # now enter the second loop to get the next score
                halfelfPlus = input("Enter the name of the second of two scores you'd like to increase: ")
                if halfelfPlus == "strength":
                    strength += 1
                    decideAgain = "yes"
                elif halfelfPlus == "dexterity":
                    dexterity += 1
                    decideAgain = "yes"
                elif halfelfPlus == "constitution": # same thing
                    constitution += 1
                    decideAgain = "yes"
                elif halfelfPlus == "intelligence":
                    intelligence += 1
                    decideAgain = "yes"
                elif halfelfPlus == "wisdom":
                    wisdom += 1
                    decideAgain = "yes"
                elif halfelfPlus == "charisma":
                    charisma += 1
                    decideAgain = "yes"
                else:
                    print("try again")
            raceChosen = True
        elif choice == "helf-elfq":
            wb.open_new_tab("https://www.dndbeyond.com/races/half-elf")

        elif choice == "halfling":
            characterRace = choice
            print("As a Halfling, "+ characterName + " gets a +2 to Dexterity.")
            dexterity += 2
            raceChosen = True
        elif choice == "halflingq":
            wb.open_new_tab("https://www.dndbeyond.com/races/halfling")

        elif choice == "half-orc":
            characterRace = choice
            print("As a Half-Orc, "+ characterName + " gets a +2 to Strength and a +1 to Constitution.")
            strength += 2
            constitution += 1
            raceChosen = True
        elif choice == "half-orcq":
            wb.open_new_tab("https://www.dndbeyond.com/races/half-orc")

        elif choice == "human":
            characterRace = choice
            print("As a Human, "+ characterName + " gets a +1 to each ability score.")
            strength += 1
            dexterity += 1          #humans get +=1 to each ability score so i just adjust this 
            constitution += 1       #for each score
            intelligence += 1
            wisdom += 1
            charisma += 1
            raceChosen = True
        elif choice == "humanq":
            wb.open_new_tab("https://www.dndbeyond.com/races/human")

        elif choice == "tiefling":
            characterRace = choice
            print("As a Tiefling, "+ characterName + " gets a +2 to Charisma and a +1 to Intelligence.")
            charisma += 2
            intelligence += 1
            raceChosen = True
        elif choice == "tieflingq":
            wb.open_new_tab("https://www.dndbeyond.com/races/tiefling")


        elif choice == "raceq" or choice == "race":
            wb.open_new_tab("https://www.dndbeyond.com/races")

        else:
            print("What you just entered isn't cool with me. Try again.")
            print("\n\n\n\n\n")

    print("You have chosen to be a "+characterRace+".") # summarize what we have just done


#def characterClass ():

    classChosen = False     #storage for this next function, character class
    choice = ""             #for the same reason i removed the def character race(): for ease
    characterClass = ""
    
    print("We are going to pick a Class now.")
    time.sleep(1)

    while classChosen == False:     #start loop
        print("These are the classes you have to choose from: ")
        time.sleep(1)               # list options
        print("Barbarian <barbarian>")
        print("Bard <bard>")
        print("Cleric <cleric>")
        print("Druid <druid>")
        print("Fighter <fighter>")
        print("Monk <monk>")
        print("Paladin <paladin>")
        print("Ranger <ranger>")
        print("Rogue <rogue>")
        print("Sorcerer <sorcerer>")
        print("Wizard <wizard>")
        time.sleep(1)
        print("If you'd like more information about something, add 'q' behind it.") # instructions to be sent to the website
        time.sleep(1)
        print("That would look something like \nclassq")
        time.sleep(1)

        choice = input("Enter your choice now: ") # get decision
        choice = choice.strip()             #remove space in front and caps
        choice = choice.lower()

        
        if choice == "barbarian":           # if decision is this
            characterClass = "barbarian"    # save it in a prettier variable
            classChosen = True              # end loop
        elif choice == "barbarianq":        # or if its the slightly different one
            wb.open_new_tab("https://www.dndbeyond.com/classes/barbarian") #take us to the website

        elif choice == "bard":
            characterClass = "bard"
            classChosen = True
        elif choice == "bardq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/bard")

        elif choice == "cleric":
            characterClass = "cleric"
            classChosen = True
        elif choice == "clericq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/cleric")

        elif choice == "druid":
            characterClass = "druid"
            classChosen = True
        elif choice == "druidq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/druid")

        elif choice == "fighter":
            characterClass = "fighter"
            classChosen = True
        elif choice == "fighterq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/fighter")

        elif choice == "monk":
            characterClass = choice
            classChosen = True
        elif choice == "monkq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/monk")

        elif choice == "paladin":
            characterClass = choice
            classChosen = True
        elif choice == "paladinq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/paladin")

        elif choice == "ranger":
            characterClass = choice
            classChosen = True              # all of these have no reason to be different
        elif choice == "rangerq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/ranger")

        elif choice == "rogue":
            characterClass = choice
            classChosen = True
        elif choice == "rogueq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/rogue")

        elif choice == "sorcerer":
            characterClass = choice
            classCChosen = True
        elif choice == "sorcererq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/sorcerer")

        elif choice == "wizard":
            characterClass = choice
            classChosen = True
        elif choice == "wizardq":
            wb.open_new_tab("https://www.dndbeyond.com/classes/wizard")


        elif choice == "classq":
            wb.open_new_tab("https://www.dndbeyond.com/sources/basic-rules/classes")

        else:
            print("Whatever you entered won't fly, bro") # catch errors 
            print("\n\n\n\n\n")                          # create space

        

    print("You have chosen to be a " + characterClass + ".") # summarize
    time.sleep(1) #style
    print("We are all finished!")                   # announce we are done
    time.sleep(1) #style 
    print("Let's get back to the main menu...")     # saving what'll happen now
    time.sleep(1) #style points


#def save():
        #save this character's information to csv
    filename = characterName + ".csv" # i want each file to be saved under the character's name, for ease of finding for user and program
    try:
        fh = open(filename, "r")     # check if the file is there 
        fh.close()
    except:
        fh = open(filename, "w")     # if not, make the storage for the character
        fh.write("Character Information\n") # add a header
        #fh.write("Name, Race, Class, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")   the first way i was saving that was more difficult to load
        fh.close()

    line1 = "\nName," + characterName
    line2 = "\nRace," + characterRace
    line3 = "\nClass," + characterClass # store each line of information
    line4 = "\nStrength," + str(strength) # str() because cannot + str and int
    line5 = "\nDexterity," + str(dexterity)
    line6 = "\nConstitution," + str(constitution)
    line7 = "\nIntelligence," + str(intelligence)
    line8 = "\nWisdom," + str(wisdom)
    line9 = "\nCharisma," + str(charisma)
    
    #lineToAdd = "\n" + characterName + "," + characterRace + "," + characterClass + "," + str(strength) + "," + str(dexterity) + "," + str(constitution) + "," + str(intelligence) + "," + str(wisdom) + "," + str(charisma) 

    try:        # keep this in a try block so if it fails, program doesnt crash
        fh = open(filename, "a") #open what we just made, and append the character info
        fh.write(line1)
        fh.write(line2)
        fh.write(line3)
        fh.write(line4)
        fh.write(line5)
        fh.write(line6)
        fh.write(line7)
        fh.write(line8)
        fh.write(line9)
        fh.close()
    except:
        print("Data not added.")





        #save the character's name in a character 'catalogue' for future viewing/loading
    try:
        fh = open("characters.txt", "r")    #check if the catalogue file has been made
        fh.close()
    except:
        fh = open("characters.txt", "w")    #if not, build it
        fh.write("List of Characters:")     #with the header
        fh.close()

    lineToAdd = "\n" + characterName        #prepare the variable that will add another line for another character to have been made

    try:
        fh = open("characters.txt", "a")
        fh. write(lineToAdd)                #add the new character to the catalogue
        fh.close()
    except:
        print("Data could not be catalogued")
        
    print("============================")
    print("\n\n\n\n\n")                     #making space for style
    print("============================")
    print("Auto saving")                    #this block is intended to hint to the user 
    time.sleep(1)                           #that I am saving what they've done 
    print(".")                              #so they can access it later
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Saving Complete.")






#also we roll stats before choosing class and race, because dont worry about it

















