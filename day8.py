
import pyfiglet
  
result = pyfiglet.figlet_format("Ceaser Cipher")
print(result)     
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=plain_text.index(letter)
        new_position=position+shift_amount
        new_text=alphabet[new_position]
        cipher_text+=new_text
    print(f'Cipher Text is {cipher_text}')




def decrypt(encoded,shift_amount):
    decipher_text=""
    for letter in encoded:
        position=encoded.index(letter)
        new_position=position-shift_amount
        new_text=alphabet[new_position]
        decipher_text+=new_text
    print(f'Deciphered Text is {decipher_text}')

if(direction=='encode'):
    encrypt(plain_text=text, shift_amount=shift)
elif(direction=='decode'):
    decrypt(encrypt=text, shift_amount=shift)
    



