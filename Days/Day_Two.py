#on this day i create a tip calculator
#Data Type
#String:
#to print a special character of a word, you can use the index function
print ("Hello"[0])

#Interger
#This mean hole number
print(123+4535)

#Float
#this are number with dot
#51351,54

#Boolean
#This mean True or False

#When you will know what Type is your Variable then do this
print (type(name_of_a_Variable))

#you can convert it into a string
new_num_char = str(name_of_a_variable)
#----------------------------------------------------------------
#praxis 1
add_num = input ("Gibe ein zweistellige Zahl ein: ")
add_num1 = add_num[0]
add_num2 = add_num[1]
print ("Das ergebnis ist: " + add_num[0] + " + " + add_num[1] + " = " )
result = int(add_num1) + int(add_num2)
print (result)

#first you save the input in two different variable, then convert it to a integer.
#-----------------------------------------------------------------
#praxis 2
#write a bmi calculator.
height = input (" Gib deine Größe in m ein( achte darauf einen Punkt, anstatt ein Komma): ")
weight = input ("Gib dein Gewicht in kg ein: ")
bmi = int(weight) / float(height) **2
bmi_as_int = int(bmi)
print (bmi_as_int)

#When you will put some digit in a score f.E.
score = 0
#User become a point
score += 1
#dont write score = score + 1

#when you have a multi Type of Dat you can use follow method to print
score = 0
height = 1.8
isWinning = True
#f-string
print(f"your Score is {score}, your height is {height} and you are winning is {isWinning}")

                                                                   
#Challenge: Your Life in Weeks
age = input ("Was ist dein aktuelles alter? ")
#365 Tage, 12 Monate, 52 Wochen bis zum ALter von 90 Jahren
week0 = 52 * 90
day0 = 365 * 90
month0 = 12 * 90
week_you = int(age) * 52
days_you = int(age) * 365
month_you = int(age) * 12
week_left = week0 - week_you
days_left = day0 - days_you
month_left = month0 - month_you
print (f"Du lebst schon {month_you} Monate, {week_you} Wochen und {days_you} Tage")
print (f"Du hast noch {month_left} Monate, {week_left} Wochen und {days_left} Tage zum Leben")


                                                                                                   
#Final Project of this Day
#Build a Tipp Calculator that divid the Count of people
print ("Welcome to the tip calculator")
bill = float(input ("What was the total bill? "))
tip = int(input ("What percentage tip would you like to give? 10,12 or 15? "))
people = int(input ("How many people to split the bill? "))
bill_with_tip = (((tip / 100 * bill) + bill) / people)
bill_with = round(bill_with_tip, 2)
print (f"Each person should pay:$ {bill_with}")