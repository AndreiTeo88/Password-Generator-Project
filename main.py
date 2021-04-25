import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_as_a_list = []

for n in range(0, nr_letters):
  password_as_a_list += random.choice(letters)

for n in range(0, nr_symbols):
  password_as_a_list += random.choice(symbols)

for n in range(0, nr_numbers):
  password_as_a_list += random.choice(numbers)


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Your password NOT randomised: {password_as_a_list}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password_as_a_list)
print(f"Your password randomised: {password_as_a_list}\n")

password = ""
for n in password_as_a_list:
  password += n

print(f"Your password is: {password}")
