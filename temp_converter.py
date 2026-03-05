# Temparature and Unit Input
try:
    temp_in_value = temp_value = float(input('Enter temperature:\n'))
except:
    print("Invalid input. Please enter a numeric temperature value.")
    exit()
temp_in_unit = input('Enter starting unit (C, F, K):\n').upper()
temp_out_unit = input('Enter target unit (C, F, K):\n').upper()

# Convert input temperature to Celsius
if temp_in_unit == 'F':
    temp_value = (temp_value - 32) * 5/9
elif temp_in_unit == 'K':
    temp_value = temp_value - 273.15
elif temp_in_unit != 'C':
    print("Invalid starting unit. Please enter C, F, or K.")
    exit()

# Check for temperatures below absolute zero
if temp_value < -273.15:
    print("Temperature cannot be below absolute zero (-273.15 C/ -459.67 F/ 0 K).")
    exit()

# Convert from Celsius to target unit
if temp_out_unit == 'F':
    temp_value = temp_value * 9/5 + 32
elif temp_out_unit == 'K':
    temp_value = temp_value + 273.15
elif temp_out_unit != 'C':
    print("Invalid target unit. Please enter C, F, or K.")
    exit()

# Output the result
print(f"{temp_in_value} {temp_in_unit} is equal to {temp_value} {temp_out_unit}.")


