import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


pass1 = [] 
for letter in range(1, nr_letters+1): 
    random_letter = random.randint(0, (len(letters)-1)) 
    pass1.append(letters[random_letter])

for sybol in range(1, nr_symbols+1): 
    random_symbol = random.randint(0, (len(symbols)-1))
    pass1.append(symbols[random_symbol])

for number in range(1, nr_numbers+1):
    random_number = random.randint(0, (len(numbers)-1))
    pass1.append(numbers[random_number])

print(f'Your new password: {"".join(pass1)}')

random_pas = []
for sign in pass1:
    randIndex = random.randint(0,(len(pass1)-1))
    random_pas.insert(randIndex, sign)
print(f'Your new randomized password: {"".join(random_pas)}')