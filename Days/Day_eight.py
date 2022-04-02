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

#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    number_can = ((height * width) /coverage)
    print ("You need "+str(math.ceil(number_can))+" cans.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
''' 
#Do NOT change any of the code below👇
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
'''
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
  
        
    

