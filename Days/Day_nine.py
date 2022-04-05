'''
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}
# to change something or add something in this dictionary you write:
programming_dictionary["Loop"] = "The action of doing something over and over again"
print (programming_dictionary)
# now the programming way:
key = input ("Input a keyword: ")
explain = input ("Input the explain for this keyword: ")
programming_dictionary[key] = explain
print (programming_dictionary)


# interactive Challenge: Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for student  in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expections"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"    
    # 🚨 Don't change the code below 👇
print(student_grades)


#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
'''
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_Country(country_visit, times_visit, cities_visit):
    new_Country = {}
    new_Country["country"] = country_visit
    new_Country["visits"] = times_visit
    new_Country["cities"] = cities_visit
    travel_log.append(new_Country)

add_new_Country("Russia", 2, ["Moscow", "Minskt"])
print(travel_log)