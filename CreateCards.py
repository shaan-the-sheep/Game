# creates number of cards based on user's input as dictionaries, using names
#from dogs.txt and generating random values for the rest. Stores these dictionaries in  a list.
#input: number of cards made (as dictionaries)
#output: list of these cards

import random

Categories = ["drool", "excercise", "friendliness", "size"]
# create dictionary of categories to help with user input
Categories_num = { 1:"friendliness", 2:"excercise", 3:"drool", 4:"size" }


def CreCards(NumOfCards, Categories):
	ListOfCards = []
	f = open("dogs.txt","r")
	ListOfNames = f.readlines()
	if NumOfCards <= len(ListOfNames):
		for x in range(NumOfCards):
			card = {}
			card['name'] = ListOfNames[x]
			random.seed()  
			card[Categories[0]] = random.randint(0,10)
			card[Categories[1]] = random.randint(0,10)
			card[Categories[2]] = random.randint(0,5)
			card[Categories[3]] = random.randint(0,10)
			ListOfCards.append(card)
	return ListOfCards
        

       
        
    
    
def PrintCard(card, whos_card):
	print(''); print('')
	print("===========================================")
	if whos_card == 1:
		print("============Your card:==================== ")
	else:
		print("============CPU's card:==================== ")
	print("dog's name: " + card['name'])
	n = 1
	for category in Categories:
		s = str(n) +") " + category + ": " + str(card[category])
		print(s)
		n += 1
	print(''); print('')
		
	