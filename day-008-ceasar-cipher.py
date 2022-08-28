from art import logo_caesar_cipher 
print("Welcome to Ceasar Cipher!")
print(logo_caesar_cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Takes the 'text', 'direction' and 'shift' as inputs. 
# Inside the function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
def ceasar(plain_text, shift_amount, cipher_direction):
  cipher_text = []
  if cipher_direction == "decode":
    shift_amount *= -1
  for character in plain_text:
    # Only cipher if it's a letter, ignore numbers & special characters
    if character in alphabet:
      index_of_character = alphabet.index(character)
      cipher_text += alphabet[index_of_character + shift_amount]
    else:
      cipher_text += character
  cipher_text = ''.join(cipher_text)
  print(f"The {cipher_direction}d text is {cipher_text}")

# Loop the game until the user says no
restart_game = True
while restart_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # If the user enter a shift number larger than 26 - which is the maximun letters in alphabet
  shift = shift % 26
  ceasar(plain_text=text, shift_amount=shift, cipher_direction=direction)

  restart_wish = input("\nDo you want to restart the game?\n").lower()
  if restart_wish == "no":
    restart_game = False
    print("Good bye.")