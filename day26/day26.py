#Editing text files with python program

from os import close, replace, write


with open("names.txt",mode="r") as names:
    name=names.read()
list=name.split()
print(type(list))

with open("letter.txt",mode="r") as letters:
    invitation=letters.read()
print(invitation)

new_letter=[]
for i in range(0,len(list)):
    file=open(f"{list[i]}.txt", mode="x")
    new_letter.append(invitation.replace("name",list[i]))
    file.write(str(new_letter[i]))
    file.close()
   

