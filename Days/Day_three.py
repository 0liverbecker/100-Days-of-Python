 #   on this Day i make a text adventure
#    Coding Exercise - Odd or Even?
#    write a program that works out whether if a given number
 #   is an odd ( can be divided by 2) or an even number
number = int (input ("Giv me a number: "))
if number % 2 == 0:
     print ("This is a odd number")
else: 
     print ("This is a even number")

#    Coding exercise - Rollercoaster
#    when your height is over 120 AND you are under 18, you pay $7
#    when your height is over 120 AND you are over 18, you pay $12
 #   when your height is under 120 you cant drive
# -----------------------------------------------
height = input ("Are you over 120 cm? (y/n)")
if height == "y" or "yes": 
     age = int(input ("How old are you? "))
     if age  < 18: 
         print ("You must pay $7 ")
     else: 
         print ("You must pay $12 ")
else: 
     print ("Sorry, you drive with the Rollercoaster")
#-------------------------------------------------------
#            Ask why the first dont work            
height = int(input ("What is your height in cm? "))
if height >= 120: 
    age = int(input ("How old are you? "))
    if age  < 12: 
        print ("You must pay $5 ")
    elif <= 18: 
       print ("You must pay $7")
    else: 
    print ("You must pay $12 ")
else: 
    print ("Sorry, you cant drive with the Rollercoaster")

#    Coding exercise - bmi 2.0
#    under 18,5 the are underweight
#    over 18,5 but below 25 they have normal weight
#    over 25 but below 30 they are overweight
#    over 30 but below 35 they are obese
#    Above 35 they are clinically obese
height = float(input("enter your height in m: "))
 weight = float(input("enter your weight in kg: "))
 #   write a class and save all colors in that class
#    then you can call it
 class color: 
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 BMI = int(weight/height**2)
 if BMI<18.5:
#    here you can call the colors but dont forget the END.
     print (f"Your BMI is {BMI}, you are ",color.RED + color.BOLD+"underweight."+color.END)
 elif (BMI>18.5 and BMI<25):
     print (f"Your BMI is {BMI}, you have a ",color.GREEN + color.BOLD + "normal weight." + color.END)
 elif (BMI>25 and BMI<30):
     print (f"Your BMI is {BMI}, you are ",color.YELLOW + color.BOLD+"slightly overweight."+color.END)
 elif (BMI>30 and BMI<35):
     print (f"Your BMI is {BMI}, you are ",color.CYAN + color.BOLD + color.UNDERLINE+ "obese."+color.END)
 elif BMI>35:
     print (f"Your BMI is {BMI}, you are ",color.RED + color.BOLD + color.UNDERLINE + "clinically obese."+color.END)
# -------------------------------------------------------------
#    Coding exercise - Leap Year
#    when a year is divid by 4, 100 and 400 without a reminder,
#    then its a Leap year
 year = int(input("Which year you want to check? "))
 if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
     print ("This is a leap year")
 else: 
     print ("This is not a leap year")
                                                                                                          



#Final Project for Day Three - Text Adventure
 print('''
 *******************************************************************************
           |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
 |                   |  ,-"_,=""     `"=.|                  |
 |___________________|__"=._o`"-._        `"=.______________|___________________
           |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 |___________________|_| ;     ( ) `-.o `"=.`_.--"_o.-; ;___|___________________
 ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 /______/______/______/______/______/______/______/______/______/______/_____ /
 *******************************************************************************
 ''')
 print("Welcome to Treasure Island.")
 print("Your mission is to find the treasure.") 
 crossroad = input ('You are at a cross road. Where do you want to go ? "left" or "right? \n').lower()
 if crossroad == "left":
     sea = input ('Youre going left an came to a sea. What would you do? "swim" oder "wait" for a boat? ').lower()
     if sea == "wait":
         door = input ('A Boat came and bring you to Island. on the this Island, you find a tunnel.\n You going in to it.\n At the End, you find three doors. Which one you will open? The "blue" Door, the "red" Door or the "yellow" Door? ').lower()
         if door == "yellow":
             print ("You find the Treasure!\n")
             print('''
             *******************************************************************************
           |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
 |                   |  ,-"_,=""     `"=.|                  |
 |___________________|__"=._o`"-._        `"=.______________|___________________
           |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 |___________________|_| ;     ( ) `-.o `"=.`_.--"_o.-; ;___|___________________
 ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 /______/______/______/______/______/______/______/______/______/______/_____ /
 *******************************************************************************
 ''')
         elif door == "blue":
             print ("You goin in a dark room. A really bad Beast came an Kills you....Game Over\n")
             print ('''.vscode\          _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
     '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')
         elif door == "red":
             print ("You going in to the red door. Fire came and burns you. You Died...Game Over. \n")
             print ('''.vscode\          _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
     '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')
         else:
             print ("You cant make a desision for long time. YOu running out of water and die...Game over \n")
             print ('''.vscode\          _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
     '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')
     elif sea == "swim":
         print ("You try to swim and a crocodil attacks you...Game Over \n")
         print ('''.vscode\          _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
     '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')
     else:
         print ("You wait to long and get attack by a bear...you died...Game over \n")
         print ('''.vscode\          _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
     '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')
 else:
     print ("You fall in to a hole and die... Game over\n")
     print ('''
               _.--._
           \ ** /
            (<>)
     .      )  (      .
     )\_.._/ /\ \_.._/(
     (*_<>_  _<>_*)
     )/ '' \ \/ / '' \(
    '      )  (      '
            (  ) 
            )  (
            (<>)
           / ** \
          /.-..-.\
              ''')