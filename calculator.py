calculation = input("Enter a calculation (e.g., 2 + 2):\n")

try:
    if calculation.split("*")[0] != calculation:
        numbers = calculation.split("*")
        result = float(numbers[0]) * float(numbers[1])
    elif calculation.split("/")[0] != calculation:
        numbers = calculation.split("/")
        if float(numbers[1]) == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        result = float(numbers[0]) / float(numbers[1])
    elif calculation.split("+")[0] != calculation:
        numbers = calculation.split("+")
        result = float(numbers[0]) + float(numbers[1])
    elif calculation.split("-")[0] != calculation:
        numbers = calculation.split("-")
        result = float(numbers[0]) - float(numbers[1])
    else:
        print("Invalid calculation format. Please use +, -, *, or /.")
        exit()
except:
    print("Invalid input. Please ensure you are entering a valid calculation.")
    exit()

print(f"The result of {calculation} is {result}.")