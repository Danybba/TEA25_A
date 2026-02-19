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

number_1 = float(input("1. Zahl: "))
number_2 = float(input("2. Zahl: "))
operation = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")

#################################################
# Calculation                                   #
#################################################

result = 0
error = False

# Add
if operation == '+':
    result = number_1 + number_2

# Sub
elif operation == '-':
    result = number_1 - number_2

# Mult
elif operation == '*':
    result = number_1 * number_2

# Div
elif operation == '/':
    try:
        result = number_1 / number_2
    except:
        error = True

# wrong operation
else:
    error = True

#################################################
# Result output                                 #
#################################################

if not error:
    print(f"Das Ergebnis ist: {result}")
else:
    print("Rechenoperation nicht unterstützt!")