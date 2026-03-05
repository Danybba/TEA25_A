# import functions as f
from functions import calculator

"""
Input:
1. Zahle: 137
2. Zahle: 5
Rechenoperation: (+) Addition (-) Subtraktion (*) Multiplikation (/) Division: /

Output:
Das Ergebnis der Rechenoperation ist: 27.4
"""

##################################################
##                                              ##
## Taschenrechner / Calculator                  ##
##                                              ##
##################################################

# author: 19.02.2026 Daniel Schäftner
# brief: Calculator with 4 basic operations

##################################################
# Usermenue input                                #
##################################################

loop = True

while loop:

    number_1 = float(input("1. Zahl: "))
    number_2 = float(input("2. Zahl: "))
    operation = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/), exit to quit: ")

    if operation == 'exit':
        loop = False

    #################################################
    # Calculation                                   #
    #################################################

    result = calculator(number_1, number_2, operation)

    #################################################
    # Result output                                 #
    #################################################

    print(f"Das Ergebnis ist: {result}")