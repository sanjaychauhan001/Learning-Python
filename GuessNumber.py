import random
secretNumber = random.randint(1,100)
print("i am thinking a number between 1 and 100")
for guesstaken in range(1,6):
    print("guess the number")
    number = int(input())
    if(number < secretNumber):
        print("you are too less")
    elif(number > secretNumber):
        print("you are too high")  
    else:
        break
if(number == secretNumber):
    print("good job! you guessed my number in " + str(guesstaken)+ "guesses!")          
else:
    print("nope the number i was thinking is " + str(secretNumber)  )

       