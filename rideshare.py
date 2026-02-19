ride_type = input("What type of ride would you like to take? (standard, plus, comfort)\n")
if ride_type == "standard":
    print("You have selected a standard ride.")
elif ride_type == "plus":
    print("You have selected a plus ride.")
elif ride_type == "comfort":
    print("You have selected a comfort ride.")
else:
    print("Invalid ride type selected. Please choose standard, plus, or comfort.")
    exit()

credits = input("How many credits do you have available?\n")
try:
    credits = float(credits)
    if credits < 0:
        print("Credits cannot be negative.")
    else:
        print(f"You have {credits} credits available.")
except ValueError:
    print("Invalid input for credits. Please enter a number.")
    exit()

if ride_type == "plus":
    ride_price = 20.5
elif ride_type == "comfort":
    ride_price = 37.9
else:
    ride_price = 18.7

if credits >= ride_price:
    print("You have enough credits to cover the entire ride.")
    final_price = 0
else:
    final_price = ride_price - credits

print(f"The remaining price of your {ride_type} ride is ${final_price:.2f}.")