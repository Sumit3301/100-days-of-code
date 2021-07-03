#Blackjack game]
import pyfiglet
  
result = pyfiglet.figlet_format("Blackjack")


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
ch=input("Do you want to play? y or n")
user_cards=random.sample(cards,k=2)
computer_cards=random.sample(cards,k=2)
if(ch=='y'):
    print(result) 
    while(True):
        print(f"Your cards are {user_cards[0]}, {user_cards[1]} and computer cards are {computer_cards[0]}")
        print(f"Your score is {sum(user_cards)} and score is {sum(computer_cards)}")
        c=input("Do you want to take more cards?")
        if(c=='y'):
            user_cards.append(random.choice(cards))

            if(sum(computer_cards)<17):
                computer_cards.append(random.choice(cards))
                print(f"Your score is {sum(user_cards)} and computer score is {sum(computer_cards)}")
        elif(c=='n'):
            out=compute_score(sum(user_cards),sum(computer_cards))
            print(f"Your score is {sum(user_cards)} and computer score is {sum(computer_cards)}")
            print(out)
            break
            
            

        






