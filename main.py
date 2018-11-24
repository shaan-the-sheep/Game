import random
#import game
import CreateCards
import DistributeCards
import PlayHand

MIN_CARDS = 2
MAX_CARDS = 28
HUMAN = 1
CPU = 2


def GetNumOfCards():
    NumOfCards = int(input("Please enter number of cards (bigger than " 
    + str(MIN_CARDS) + ", less than " + str(MAX_CARDS) + ", even number): "))
    if NumOfCards > MIN_CARDS and NumOfCards < MAX_CARDS:
        if NumOfCards % 2 == 0:
            return NumOfCards
    return -1

   
def GetCategory(winner):
    if winner == HUMAN:
        while True:
            selection = raw_input("Please select a category number from your card above [1,2,3,4]: ")
            if selection == "Q" or selection == "Quit" or selection == "q":
                exit(-1)
            if int(selection) in CreateCards.Categories_num:
                return CreateCards.Categories_num[int(selection)]
    else:
        num = random.randint(1, 4)
        category = CreateCards.Categories_num[num]
    return category

def ShowCard(list,player):
    card = list[0]
    CreateCards.PrintCard(card, player)
    

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
    
    cards = CreateCards.CreCards(NumOfCards, CreateCards.Categories)
    list1,list2 = DistributeCards.DisCards(cards)
    """print("This is list 1: ",list1)
    print()
    print()
    print("This is list 2: ",list2)"""
    
    # start game until one list is empty
    winner = HUMAN    # first hand, make human winner
    while len(list1)!= 0 and len(list2)!= 0:
        if winner == HUMAN:
            ShowCard(list1,HUMAN)
            category = GetCategory(winner)
            ShowCard(list2,CPU)
        else:
            ShowCard(list1,HUMAN)
            category = GetCategory(winner)
            ShowCard(list2,CPU)
            print("The CPU chose the category: ", category)
        winner,list1,list2 = PlayHand.PlayHand(list1,list2,category)
        if winner == HUMAN or winner == None:
            print("You won the round! Congratulations!")
        else:
            print("Oh No! The CPU has won this round.")
    if len(list1) == 0:
        print("Game over/nThe overall winner is the CPU! Better luck next time!")
    else:
        print("Game over/nYou won the overall game! Congratulations!")
    
PlayGameMain()     
    


        
