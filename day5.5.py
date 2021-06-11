#Building a password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers=['1','2','3','4','5','6','7','8','9','10']
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbol=int(nr_symbols)
nr_letter=int(nr_letters)
nr_number=int(nr_numbers)
letter=random.sample(letters,k=nr_letter)
symbol=random.sample(symbols,k=nr_symbols)
number=random.sample(numbers,k=nr_numbers)
passwor=letter+symbol+number
random.shuffle(passwor)
password=''.join(passwor)
print(password)

