# CreateCards
# creates number of cards based on user's input as dictionaries, using names
#from dogs.txt and generating random values for the rest. Stores these dictionaries in  a list.
#input: number of cards made (as dictionaries)
#output: list of these cards

import random
import os

HUMAN = 1
CPU = 2
MIN_CARDS = 2
MAX_CARDS = 28

Categories = ["drool", "excercise", "friendliness", "size"]
# create dictionary of categories to help with user input
Categories_num = { 1:"drool", 2:"excercise", 3:"friendliness", 4:"size" }

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
	

# DistributeCards
''' splits a list in two. returns the two lists as a tuple '''
def DisCards(ListOfCards):
	# Extra safety check
	if len(ListOfCards) % 2 == 0:
		list1 = ListOfCards[:int(len(ListOfCards)/2)]
		list2 = ListOfCards[int(len(ListOfCards)/2):]
		return list1, list2
		

#PlayHand
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
        

# main
def GetNumOfCards():
    NumOfCards = int(input("Please enter number of cards (bigger than " 
    + str(MIN_CARDS) + ", less than " + str(MAX_CARDS) + ", even number): "))
    if NumOfCards > MIN_CARDS and NumOfCards < MAX_CARDS:
        if NumOfCards % 2 == 0:
            return NumOfCards
    return -1

def GetCategory(winner):
    if winner == HUMAN:
        while True:
            selection = raw_input("Please select a category number from your card above [1,2,3,4]: ")
            if selection == "Q" or selection == "Quit" or selection == "q":
                exit(-1)
            if int(selection) in Categories_num:
                return Categories_num[int(selection)]
    else:
        num = random.randint(1, 4)
        category = Categories_num[num]
    return category

def ShowCard(list,player):
    card = list[0]
    PrintCard(card, player)
    
def DisplayMainMenu():
    choice = int(input("CELEBRITY DOGS\nPlease choose an option: \n1) Play Game \n2) Quit Program \n"))
    return choice

def IsGameFinished(list1,list2):
    if len(list1) > 0 and len(list2) > 0:
        return False 
    else:
        return True
        
def PlayGameMain():
    """ this is the main function that gets called by main
    """
    CPU_score = 0
    HUMAN_score = 0
    
    while True:
        choice = DisplayMainMenu()    
        if choice == 2: 
            # do_exit
            exit(-1)
        # currently display menu only has 2 options
        # code below heavily depends on that
        elif choice != 1:
            continue
        NumOfCards = GetNumOfCards()
        if NumOfCards != -1:
            break
        print("\nERROR: The number you have entered is invalid\n")
    
    cards = CreCards(NumOfCards, Categories)
    list1,list2 = DisCards(cards)
    
    # start game until one list is empty
    winner = HUMAN    # first hand, make human winner
    while len(list1)!= 0 and len(list2)!= 0:
        if winner == HUMAN:
            ShowCard(list1,HUMAN)
            category = GetCategory(winner)
            ShowCard(list2,CPU)
        else:
            ShowCard(list1,HUMAN)
            category = GetCategory(winner)
            ShowCard(list2,CPU)
            print("The CPU chose the category: " + category)
        #if len(list1) > 0 and len(list2) > 0:
        if not IsGameFinished(list1,list2):
            raw_input("Press enter to reveal winner: ")
        winner,list1,list2 = PlayHand(list1,list2,category)
        if winner == HUMAN:
            print("You won the round! Congratulations!")
            HUMAN_score += 1
        elif winner == CPU:
            print("Oops! The CPU has won this round.")
            CPU_score += 1
            
        #if len(list1) > 0 and len(list2) > 0:
        if not IsGameFinished(list1,list2):
            raw_input("Press enter to see your next card: ")
            os.system('clear') 
            print("CPU's score = " + str(CPU_score) + " Your score = " + str(HUMAN_score))
    if len(list1) == 0:
        print("Game over\nThe overall winner is the CPU! Better luck next time!")
    else:
        print("Game over\nYou won the overall game! Congratulations!")
    
PlayGameMain() 
        


