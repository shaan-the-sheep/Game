def PlayHand(card1, card2, category):
    a = card1[category]
    b = card2[category]
    if a == b:
        return None
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

def TransferCards(list1,list2,category):
    card1 = list1[0]
    card2 = list2[0]
    winner = PlayHand(card1,card2,category)
    if winner == card1:
        # list1 has won this hand.
        # winning card moves from front to back of list1.
        # losing card is removed from list2 and placed at back of list1.
        list1.remove(card1)
        list1.append(card1)
        list2.remove(card2)
        list1.append(card2)
    else:
        # list2 has won this hand.
        # winning card moves from front to back of list2.
        # losing card is removed from list1 and placed at back of list2.
        list2.remove(card2)
        list2.append(card2)
        list1.remove(card1)
        list2.append(card1)
     # for debug
    return list1,list2
        
        
    
