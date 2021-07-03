#Number Guessing Game
import random
number=random.randrange(40)
diff=input("Enter your difficulty level , easy, medium or hard")
if(diff=='easy'):
    life=10
elif(diff=='medium'):
    life=7
elif(diff=='hard'):
    life=5

while(life!=0):
    guess=input("Enter your guess")
    if(guess<number):
        print(" Low")
        life-=1
    elif(guess>number):
        print("Too high")
        life-=1
    elif(guess==number):
        print("Correct answer")




