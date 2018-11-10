import game
MIN_CARDS = 2
MAX_CARDS = 28

'''def menu():
choice = int(input("1) Play Game \n 2)Quit Program \n Please choose an option: "))
if choice == 1:

else: '''


def GetNumOfCards():
    NumOfCards = int(input("Please enter number of cards (bigger than " 
    + str(MIN_CARDS) + ", less than " + str(MAX_CARDS) + ", even number): "))
    if NumOfCards > MIN_CARDS and NumOfCards < MAX_CARDS:
        if NumOfCards % 2 == 0:
            return NumOfCards
    return -1
            

#ToDo: assess who the winner is!
'''        list1,list2 = game.game(NumOfCards,category)
        if len(list1) == 0:
            winner = list2
        else:
            winner = list1
        return winner '''
        
