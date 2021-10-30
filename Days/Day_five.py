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
total = 0
for number in range(2, 100, 2): 
    total += number 
print (total) 