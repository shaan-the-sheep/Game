import CreateCards

f = open("TestFile_CreateCards.txt","r")
lines = f.readlines()
for num in lines:
    num = int(num) 
    cards = CreateCards.CreCards(num)
    # ToDo check for neg num!!
    #if num < 0:
      
    if num == len(cards):
        print("yay, card num:", num)
    else:
        print("oh no, card num:", num)
