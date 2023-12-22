import random , sys

wins = 0
losses = 0
ties = 0
print("welcome to snake water gun game")
while True:
    print("%s wins , %s Losses , %s Ties " %(wins, losses , ties))
    print("enter your move 1 for sanke, 2 for water, 3 for Gun and 0 for quit :")
    user = int(input())

    if(user == 0):
        print("game over")
        sys.exit()

    if(user == 1):
        print("snake versess....", end='')
    elif(user == 2):
        print("water versess....",end='')    
    elif(user == 3):
        print("gun versess....",end='')  

    computer = random.randint(1,3)
    if(computer == 1):
        print("sanke")
    elif(computer == 2):
        print("water")    
    elif(computer == 3):
        print("gun")    

    if(user == computer):
        print("it is a tie ")       
        ties = ties+1
    elif(user == 1 and computer == 2  ):
        print("you win")    
        wins = wins+1
    elif(user == 2 and computer == 3):
        print("you win")    
        wins = wins + 1   
    elif(user == 3 and computer == 1):
        print("you win")    
        wins = wins + 1 

    if(computer == 1 and user == 2):
        print("you lose!")         
        losses = losses+1
    elif(computer == 2 and user == 3):
        print("you lose!")    
        losses = losses+1
    elif(computer == 3 and user == 1):
        print("you lose!")    
        losses = losses+1
    