''' splits a list in two. returns the two lists as a tuple '''
def DisCards(ListOfCards):
	# Extra safety check
	if len(ListOfCards) % 2 == 0:
		list1 = ListOfCards[:int(len(ListOfCards)/2)]
		list2 = ListOfCards[int(len(ListOfCards)/2):]
		return list1, list2
	
