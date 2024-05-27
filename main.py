#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#USING FOR LOOP
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_gen = ""

for letter in range(1, nr_letters + 1):
  password_gen += random.choice(letters)
for symbol in range(1, nr_symbols + 1):
  password_gen += random.choice(symbols)
for number in range(1, nr_numbers + 1):
  password_gen += random.choice(numbers)

print(password_gen)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for letter in password_list:
  password += letter

print(f"Your password is: {password}")

#-----------------------
#WITHOUT FOR LOOP
#Eazy Level - Order not randomised:

rand_letters = ''.join(random.choice(letters) for x in range(nr_letters))
rand_symbols = ''.join(random.choice(symbols) for x in range(nr_symbols))
rand_numbers = ''.join(random.choice(numbers) for x in range(nr_numbers))

password = rand_letters + rand_symbols + rand_numbers
print(password)
#------------------------

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

new_password = ''.join(random.sample(password, len(password)))

print(f"Your password is: {new_password}")