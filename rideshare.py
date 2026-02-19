ride_type = input("What type of ride would you like to take? (standard, plus, comfort)\n")
if ride_type == "standard" or ride_type == "plus" or ride_type == "comfort":
    print(f"You have selected a {ride_type} ride.")
else:
    print("Invalid ride type selected. Please choose standard, plus, or comfort.")
    exit()

credits = input("How many credits do you have available?\n")
try:
    credits = float(credits)
    if credits < 0:
        print("Credits cannot be negative.")
        exit()
    else:
        print(f"You have {credits} remaining credits.")
except:
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