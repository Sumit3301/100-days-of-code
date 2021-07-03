#Number Guessing Game
import random

diff=input("Enter your difficulty level , easy, medium or hard")
if(diff=='easy'):
    life=10
elif(diff=='medium'):
    life=7
elif(diff=='hard'):
    life=5

while(life==0):
