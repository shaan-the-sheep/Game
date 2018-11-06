import CreateCards
import DistributeCards
import PlayHand 
NumOfCards = 24

cards = CreateCards.CreCards(NumOfCards)
list1,list2 = DistributeCards.DisCards(cards)

while len(list1)!= 0 and len(list2)!= 0:
    list1,list2 = PlayHand.PlayHand(list1,list2,"size")
if len(list1) > len(list2):
    print("winner = list1")
else:
    print("winner = list2")
