student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)): 
    student_scores[n] = int(student_scores[n])
print(student_scores)

#   i set the highest score on 0 and then i search with a Loop, which is the highest score later
highest_score = 0 ## high on 0
for score in student_scores: ## for every score in student_score do this?
    if score > highest_score: ## ask if position 0 higher as high = now if pos 1 high as...and this so long until the highest is found
        highest_score = score ## then put this highest score in this variable
print (f"The highest Score in the class is: {highest_score}") ## print it out