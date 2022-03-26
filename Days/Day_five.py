# Day_five
## Coding exercise - High Score Calc
###################################################################################################
# Here you give me information and separate it with a space, so i can make a List
#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)): 
#    student_scores[n] = int(student_scores[n])
#print(student_scores)
#
#   i set the highest score on 0 and then i search with a Loop, which is the highest score later
#highest_score = 0 ## high on 0
#for score in student_scores: ## for every score in student_score do this?
#    if score > highest_score: ## ask if position 0 higher as high = now if pos 1 high as...and this so long until the highest is found
#        highest_score = score ## then put this highest score in this variable
#print (f"The highest Score in the class is: {highest_score}") ## print it out
#
#####################################################################################################
#   Range Loops
#for number in range(1, 11): ## i store a range 1 to 11 in the variable range
#    print (number) ## for every pos i print until i end the range-list
    
#for number in range(1, 11, 3): ## when i put a third number in this list, it mean the stepsize that the program make
 #   print (number)

# now i make a starting point with total and store a list from 1 to 101
#total = 0
#for number in range(1, 101): 
#    total += number # here the program sum every number in my list: total+1=1,total+2=3, total+3= 6...
#print (total) # when you make the print with a tab under the total, ever step is printed
########################################################################################################
#   Coding exercise - Adding evens
#   You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
#   Thus, the first even number would be 2 and the last one is 100:
#   i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#   Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#   There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
# My Solution 
#total = 0
#for number in range(2, 101, 2): 
#    total += number 
#print (total) 
#########################################################################################################
#   The Fizz Buzz Exercise
#   Your program should print each number from 1 to 100 in turn.
#   When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#   When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
# my Solution
#for number in range (1, 100):
#    if number % 3  :
#        print ("Fizz")
#    elif number % 5 :
#        print ("Buzz")
#    elif number % 3 and number % 5 :
#        print ("FizzBuzz")
#    else:
#        print (number)
#print (number)
#   this was my first idea, but it print only fizz and buzz. 
#for number in range (1, 100):
#    if number % 3 == 0 :
#        print ("Fizz")
#    elif number % 5 == 0:
#        print ("Buzz")
#    elif number % 3 == 0 and number % 5 == 0:
#        print ("FizzBuzz")
#    else:
#        print (number)
#print (number)
#   now it print the 3 and 5 out, but not the FzzBuzz statement. 
#   the problem is that the program skip to 3and5 when the first is right. 
#for number in range (1, 100):
#    if number % 3 == 0 and number % 5 == 0:
#        print ("FizzBuzz")
#    elif number % 3 == 0 :
#        print ("Fizz")
#    elif number % 5 == 0:
#        print ("Buzz")
#    else:
#        print (number)
#print (number)
#   now is right, i write the and function first. now is it right
#################################################################################################
#   Final Challenge - Passwort Generator
#Password Generator Project
# first i store letters/ numbers and symbol in variable
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# then i write the text and store the input in another variable
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass1 = [] ## then i make a list for passwd 
for letter in range(1, nr_letters+1): # i make a range from 1 to choice 
    random_letter = random.randint(0, (len(letters)-1)) # then put a random letter form my list and store it to the pass1
    pass1.append(letters[random_letter])

for sybol in range(1, nr_symbols+1): # i do the same for the other variable 
    random_symbol = random.randint(0, (len(symbols)-1))
    pass1.append(symbols[random_symbol])

for number in range(1, nr_numbers+1):
    random_number = random.randint(0, (len(numbers)-1))
    pass1.append(numbers[random_number])
# now i have a Bunch of characters in pass1, in order letter, symbol and numbers
print(f'Your new password: {"".join(pass1)}')

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# to randomized this passwort, i make a new variable and say passwd is my list, it has len.(diggits) and now give me a random from pass1 until the list is end
random_pas = []
for sign in pass1:
    randIndex = random.randint(0,(len(pass1)-1))
    random_pas.insert(randIndex, sign)
print(f'Your new randomized password: {"".join(random_pas)}')
