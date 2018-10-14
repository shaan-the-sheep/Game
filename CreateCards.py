# creates number of cards based on user's input as dictionaries, using names
#from dogs.txt and generating random values for the rest. Stores these dictionaries in  a list.
#input: number of cards made (as dictionaries)
#output: list of these cards
ListOfCards = []
AttrTypes = ["friendliness", "excercise", "drool", "size"]
import random
def CreCards(NumOfCards):
	f = open("dogs.txt","r")
	ListOfNames = f.readlines()
	if NumOfCards <= len(ListOfNames):
		for x in range(NumOfCards):
			card = {}
			card['name'] = ListOfNames[x]
			random.seed()  
			card[AttrTypes[0]] = random.randint(0,10)
			card[AttrTypes[1]] = random.randint(0,10)
			card[AttrTypes[2]] = random.randint(0,5)
			card[AttrTypes[3]] = random.randint(0,10)
			ListOfCards.append(card)
	return ListOfCards
        

       
        
    
    
