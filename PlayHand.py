#from main import HUMAN
#from main import CPU

HUMAN = 1
CPU = 2

def CompareCards(card1, card2, category):
    a = card1[category]
    b = card2[category]
    #print ("*** a: %d, b: %d" % (a, b))
    if a == b:
        #print ("*** Equal values Make Human win")
        return card1  # human always wins if equal
    elif category == "drool":
        if a > b:
            winner = card2
        else:
            winner = card1
        return winner 
    else:
        if a > b:
            winner = card1
        else:
            winner = card2
        return winner
     

def PlayHand(list1,list2,category):
    card1 = list1[0]
    card2 = list2[0]
    winner = CompareCards(card1,card2,category)
    if winner == card1:
        # list1 has won this hand.
        # winning card moves from front to back of list1.
        # losing card is removed from list2 and placed at back of list1.
        list1.remove(card1)
        list1.append(card1)
        list2.remove(card2)
        list1.append(card2)
        return HUMAN,list1,list2
    else:
        # list2 has won this hand.
        # winning card moves from front to back of list2.
        # losing card is removed from list1 and placed at back of list2.
        list2.remove(card2)
        list2.append(card2)
        list1.remove(card1)
        list2.append(card1)
        return CPU,list1,list2

        
    
