#Blackjack game]
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while(True):
    choice=input("Do you want to play or not?")
    if(choice=='y'):
        user_cards=random.sample(cards,k=2)
        print(f'Your cards {user_cards}')
        comp_card=random.sample(cards,k=2)
        print(f'Computer cards {comp_card[0]}')
       





