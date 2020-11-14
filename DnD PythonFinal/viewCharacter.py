

#view characters
def view():
    print("\n\n\n")
    try:
        fh = open("characters.txt", "r")        # make sure my catalogue is there
        print("Which character would you like to look at?")
        for line in fh:
            print(line)                         #list off each saved character's name
        print("\n\n\n")
        viewCharacter = input("\nType the name of the dude you'd like to check out:")
        fh.close()
    except:                                     # if this throws, then there must not be a save file made
        print("There are no saved characters, my dude.")

    filename = viewCharacter + ".csv"           # making sure that the file that is opened is the character the user wants
    try:
        fh = open(filename, "r")
        fh.close()
    except:                                     # if nothing pulls up, user didnt enter a name correctly
        print("Data not retrieved. Check spelling and try again.")


    print("\n\n\n")
        # cool, by this point we have a character file picked out
    fh = open(filename, "r")
    for line in fh:     #lets grab the contents
        line = line.strip("\n") 
        print(line)     #and put them onto the screen

    fh.close()


    print("\n\n\n")


#view()
# commented out, so i can test it solo if i need to
