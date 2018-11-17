import game
MIN_CARDS = 2
MAX_CARDS = 28

def GetNumOfCards():
    NumOfCards = int(input("Please enter number of cards (bigger than " 
    + str(MIN_CARDS) + ", less than " + str(MAX_CARDS) + ", even number): "))
    if NumOfCards > MIN_CARDS and NumOfCards < MAX_CARDS:
        if NumOfCards % 2 == 0:
            return NumOfCards
    return -1

def DisplayMainMenu():
    choice = int(input("CELEBRITY DOGS\nPlease choose an option: \n1) Play Game \n2) Quit Program \n"))
    return choice
    
    
def PlayGameMain():
    """ this is the main function that gets called by main
    """
    while True:
        choice = DisplayMainMenu()    
        if choice == 2: 
            # do_exit
            exit(-1)
        # currently display menu only has 2 options
        # code below heavily depends on that 
        NumOfCards = GetNumOfCards()
        if NumOfCards != -1:
            break
        print("\nERROR: The number you have entered is invalid\n")
    list1,list2 = game.game(NumOfCards)
    print(list1)
    print()
    print(list2)
    


        
