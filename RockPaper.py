import random, sys

print("Rock Paper Scissor")
wins = 0
losses = 0
ties = 0
 
while True: 
    print("%s wins , %s Losses , %s Ties " %(wins, losses , ties))
    while True:
        print("Enter your move: (r)ock , (p)aper, (s)cissor, (q)uit ")
        userinput = input()
        if(userinput == "q"):
          sys.exit()
        if(userinput == "r" or userinput =="p" or userinput== "s"):  
            break

    if(userinput == "r"):
        print("rock versess...", end= " ")
    elif(userinput == "p"):
        print("paper versess...",end= " ")
    elif(userinput == "s"):
        print("scissor versses...",end= " ")

    randomNumber = random.randint(1,3)    
    if(randomNumber == 1):
        computerMove = "r"
        print("ROCK")
    elif(randomNumber == 2):
        computerMove = "p"
        print("PAPER")
    elif(randomNumber == 3):
        computerMove = "s"    
        print("SCISSOR")

    if(userinput == computerMove):
        print("it is a tie")    
        ties = ties+1
    elif(userinput == "p" and computerMove =="r"):
        print("you win..")    
        wins = wins+1
    elif(userinput == "r" and computerMove == "s"):
          print("you win..")    
          wins = wins+1  
    elif(userinput == "s" and computerMove == "p"):
          print("you win..")    
          wins = wins+1      
    elif(userinput == 'r' and computerMove == 'p'):
        print('You lose!')
        losses = losses + 1
    elif(userinput== 'p' and computerMove == 's'):
       print('You lose!')
       losses = losses + 1
    elif(userinput == 's' and computerMove == 'r'):
       print('You lose!')
       losses = losses + 1      