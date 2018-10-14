import CreateCards
import DistributeCards
NumOfCards = 24


cards = CreateCards.CreCards(NumOfCards)
list1,list2 = DistributeCards.DisCards(cards)
print(list1,list2)

