from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_input, user_message, shift_number):
  end_message = ""
  if user_input == "decode":
      shift_number *= -1
  for char in user_message:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_number
      new_letter = alphabet[new_position]
      end_message += new_letter
    else:
      end_message += char
  
  print("The " + user_input + "d message is " + end_message)

cont = True

while cont:
  user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  user_message = input("Type your message:\n").lower()
  shift_number = int(input("Type the shift number:\n"))
  shift_number = shift_number % 26

  caesar(user_input, user_message, shift_number)

  user_cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if user_cont == "no":
    cont = False
    print("Goodbye!")
    
  





          