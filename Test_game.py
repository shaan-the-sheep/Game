import game


f = open("TestFile_main.txt","r")
lines = f.readlines()
for num in lines:
    num = int(num) 
    list1,list2 = game.game(num)
    
    if len(list1) == 0:
        if len(list2) == num:
            print("yay, card num:", num)
        else:
            print("oh no, card num:", num)
    else:
        if len(list2) == 0:
            if len(list1) == num:
                print("yay, card num:", num)
            else:
                print("oh no, card num:", num)
        else:
            print("oh no, card num:", num)
                   
        
