''' in this Lesson i write a program that Encrypt Data and encrypt this.

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#def greet():
#    print ("number one")
#    print ("number two")
#    print ("number three")
#greet()
# now we do the same but with a input
#def greet_with(name):
#    print (f"hey {name}")
#
#greet_with("oli")

#Write your code below this line ๐
import math
def paint_calc(height, width, cover):
    number_can = ((height * width) /coverage)
    print ("You need "+str(math.ceil(number_can))+" cans.")


#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
''' 
#Do NOT change any of the code below๐
''' Here is my Solution for a Prime Checker
primzahlen =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def primecheck():
    n = int(input("Check this number (only 2 digits): "))
    if n in primzahlen:
        print (f"{n} ist eine Primzahl.")
    else:
        print (f"{n} ist keine Primzahl.")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        primecheck()
    else:
        print("Goodbye")
primecheck()

# here is the right solution

def prime_checker(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print ("Its a prime number.")
    else:
        print("Its not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
'''
# my solution for the ceasar cipher challenge:
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    ausgabetext = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        ausgabetext += new_letter
    print (f"Der geheime Code lautet :{ausgabetext}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        ceasar()
    else:
        print("Goodbye")

def ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  
    if direction == "decode":
        encrypt(text, shift)
    else:
        shift = (26-shift)
        encrypt(text, shift)

ceasar()    
'''

