#Rock Paper Scissor game
import random
ip=int(input("Enter Rock(0) Paper(1) or Scrissor(2)"))
computer=random.randint(0,2)
if(ip==0):
    print("Human -->Rock")
if(ip==1):
    print("Human -->Paper")
if(ip==2):
    print("Human -->Scissor")
if(computer==0):
    print("Computer -->Rock")
if(computer==1):
    print("Computer -->Paper")
if(computer==2):
    print("Computer -->Scissor")

if(ip!=computer):
    if(ip==0):
        if(computer==1):
            print("You failed")
        else:
            print("Passed")
    if(ip==1):
        if(computer==2):
            print("You Failed")
        else:
            print("You passed")
    if(ip==2):
        if(computer==0):
            print("Your Failed")
        else:
            print("You passed")

elif(ip==computer):
    print('Its a tie')

    