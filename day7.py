#hangman game
import random
word_list=['andaman','nicobar','island']
chosen_word=random.choice(word_list)
print(chosen_word)
inp=input("Enter a character")
inp.lower()
for i in range(0,len(chosen_word)):
    if(chosen_word[i]!=inp):
        print("__",end=" ")
    else:
        print(inp,end=' ')