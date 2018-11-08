import CreateCards
import DistributeCards
import PlayHand 

def game(NumOfCards):
    print("starting new game with num of cards: ", NumOfCards)
    cards = CreateCards.CreCards(NumOfCards)
    list1,list2 = DistributeCards.DisCards(cards)

    while len(list1)!= 0 and len(list2)!= 0:
        list1,list2 = PlayHand.PlayHand(list1,list2,"size")
    return list1,list2


'''
if __name__ == "__main__":
    # we know this module has been invoked from the
    # command line
    print "SHOULD NOT SEE THIS"
    list1,list2 = game(24)
'''    