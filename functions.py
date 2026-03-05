import datetime

# print("Aktuelles Datum und Uhrzeit:", datetime.datetime.now())
# print(datetime.datetime.now().year )

# function definition
def welcome_message():
    print("Willkommen zum Taschenrechner!")
    print("Du kannst hier 4 Grundrechenarten durchführen.")
    
def double_number(number):
    return number * 2

def half_number(number):
    return number / 2

def add_numbers(number_1, number_2):
    return number_1 + number_2

def subtract_numbers(number_1, number_2):
    return number_1 - number_2

def multiply_numbers(number_1, number_2):
    return number_1 * number_2

def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Fehler: Division durch Null ist nicht erlaubt!"


def calculator(number_1, number_2, operation):
    if operation == '+':
        return add_numbers(number_1, number_2)
    elif operation == '-':
        return subtract_numbers(number_1, number_2)
    elif operation == '*':
        return multiply_numbers(number_1, number_2)
    elif operation == '/':
        return divide_numbers(number_1, number_2)
    else:
        return "Fehler: Rechenoperation nicht unterstützt!"
    

# main programm
# greet_user("Anna", "Müller", 25)

# greet_user("Emil", "Schmidt", 30)

# greet_user("User", "Mustermann", 40)

# print(double_number(5))
# print(half_number(10))
# print(add_numbers(5, 3))
# print(subtract_numbers(10, 4))
# print(multiply_numbers(5, 3))
# print(divide_numbers(10, 2))
# print(divide_numbers(10, 0))    

# print(calculator(5, 3, '+'))

# import math as m
# # from math import pi

# print(m.pi)