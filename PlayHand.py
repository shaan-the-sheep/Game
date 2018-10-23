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
    