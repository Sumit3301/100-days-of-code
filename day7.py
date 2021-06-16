#hangman game
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=['andaman','nicobar','island']
chosen_word=random.choice(word_list)
lis=list(chosen_word)
print(lis)
print(chosen_word)
display=[]
for i in range(0,len(chosen_word)):
    display+=['']
k=0
while(k<=len(chosen_word)):
    k=k+1
    inp=input("Enter letter: ").lower()
    for j in range(0,len(chosen_word)):
        if(chosen_word[j]==inp):
            display[j]=inp
            print(display)

if('' not in display):
    print("You Win")
else:
    print("You loose")
print(f'Correct word is {chosen_word}')
