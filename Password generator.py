import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symb = int(input(f"How many symbols would you like?\n"))
nr_numb = int(input(f"How many numbers would you like?\n"))


strl=""
for i in range(0,nr_letters):
  strl+= random.choice(letters)
  # strl+=randl 
for i in range(0,nr_symb):
  strl+= random.choice(symb)

for i in range(0,nr_numb):
  strl+= random.choice(numb)





x=list(strl)
random.shuffle(x)

print("Your random password is: "+''.join(x))
