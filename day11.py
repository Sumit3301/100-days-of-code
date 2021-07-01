#Blackjack game]
def compute_score(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
         return "You went over. You lose 😤"


    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
       return "You win 😃"
    else:
       return "You lose 😤"

       
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while(True):
    choice=input("Do you want to play or not?")
    if(choice=='y'):
        user_cards=random.sample(cards,k=2)
        print(f'Your cards {user_cards}')
        comp_card=random.sample(cards,k=1)
        print(f'Computer cards {comp_card[0]}')
    choice1=input("Do you want to add another card?")
    if(choice1=='y'):
        user_cards=user_cards.append(random.sample(cards,k=1))
    if(choice1=='n'):
        compute_score(user_cards,comp_card)
        break

        






