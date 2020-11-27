print("this program rolls a dice and tells you what the roll is called\n")
input("Press enter to get started")
  
dicerolls = {
    (1, 1): "\nsnake eyes",
    (1, 2): "\nAustralian yo",
    (1, 3): "\nLittle joe from kokomo",
    (1, 4): "\nNo field five",
    (1, 5): "\nEasy six",
    (1, 6): "\nSix one you're done",
    (2, 1): "\nAce caught a deuce",
    (2, 2): "\nBallerina",
    (2, 3): "\nMicheal Jordan",
    (2, 4): "\nJimmie Hicks",
    (2, 5): "\nBenny Blue",
    (2, 6): "\nEasy eight",
    (3, 1): "\nEasy four",
    (3, 2): "\nThe fever",
    (3, 3): "\nBrooklyn forest",
    (3, 4): "\nBig red",
    (3, 5): "\nEighter from decatur",
    (3, 6): "\nNina from Pasadena",
    (4, 1): "\nLittle Phoebe",
    (4, 2): "\nLumber Number",
    (4, 3): "\nSkinny Mckinney",
    (4, 4): "\nSquare pair",
    (4, 5): "\nRailroad nine",
    (4, 6): "\nBig one on the end",
    (5, 1): "\nSixie from Dixie",
    (5, 2): "\nSkinny Dugan",
    (5, 3): "\nEasy Eight",
    (5, 4): "\nJesse James",
    (5, 5): "\nPuppy Paws",
    (5, 6): "\nYo",
    (6, 1): "\nThe Devil",
    (6, 2): "\nEasy eight",
    (6, 3): "\nLou Brown",
    (6, 4): "\nTennessee",
    (6, 5): "\nSix five no jive",
    (6, 6): "\nMidnight",
}


def roll_dice():
    loop = True
    while loop:
        import random

        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        result = (roll1, roll2)
       
        print(result)
        print(dicerolls.get(result) + "\n")

        if input("type yes to go again, otherwise the program will close: ") == "yes":
            loop = True
        else:
            print("closing program")
            loop = False


roll_dice()



