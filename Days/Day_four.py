#   End of this Day i build a Paper and scissors Game
#   When you have a Modul and you will know, what it can do: go an askpython.com and google it
# import random 
#   zuerst das module importieren 
# random_integer = random.randint(100, 200)
#   hier wird nun eine zahl zwischen 100 und 200 gewählt und ausgedruckt
# print (random_integer)
#   module umfassen bspw vaiabeln : Modul my_module hat : pi = 3.14
#   wenn ich nun in einem anderen project diese variable auf rufen möchte, importiere ich sie und 
#   print(modulename.varaible)  -    print (my_module.pi)
############################################################################################################
#   Coding Challenge - Coinflip Game
# import random
# coin = random.randint(1,2)
# if coin == 1:
#    print ("Heads")
# else:
#    print ("Tails")
############################################################################################################
#   Coding Challenge - Tip Rolette
#   You write a Name with komma: olli, jessi, eve ... and then the Programm pick a Random name from this List
#import random
#name_rolette = input(" Write all the names that you have on the table, split it with a comma: ").lower()
#op = name_rolette.split(", ")
#name_rolette_count = len(op)
#tip_n = random.randint(0, name_rolette_count)
#print (op[tip_n - 1]+" bezahlt heute.")
#############################################################################################################
#   Final Challenge of the Day - Stein Schere Papier
stein = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

schere = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
sign = [stein, schere, papier]
import random
ai = random.randint(0,2)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if ai == 0 and choice == 1:
    print ("Deine Wahl " + sign[choice])
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Stein. Stein schlägt Schere. KI gewinnt")
elif ai == 0 and choice == 0:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Stein. Stein und Stein geht nicht. Niemand gewinnt")    
elif ai == 0 and choice == 2:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Stein. Papier schlägt Stein. Du gewinnst")
elif ai == 1 and choice == 0:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Schere. Stein schlägt Schere. Du gewinnst")
elif ai == 1 and choice == 1:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Schere. Schere und Schere geht nicht. Niemand gewinnt")
elif ai == 1 and choice == 2:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Schere. Schere schlägt Papier. KI gewinnt")
elif ai == 2 and choice == 0:
    print ("Deine Wahl " + sign[choice] )
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Papier. Stein schlägt Papier. KI gewinnt")
elif ai == 2 and choice == 1:
    print ("Deine Wahl " + sign[choice])
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Papier. Schere schlägt Papier. Du gewinnst")
elif ai == 2 and choice == 2:
    print ("Deine Wahl " + sign[choice])
    print ("KI wählt "+sign[ai])
    print ("Die KI nimmt Papier. Papier und Papier geht nicht. Niemand gewinnt")
else:
    print ("Falsche Eingabe")