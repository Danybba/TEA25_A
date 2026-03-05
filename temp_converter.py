#########################
# Temperature Converter #
#########################
# author: Linus
# brief: A simple temperature converter that converts between Celsius, Fahrenheit, and Kelvin.

# Constants for temperature conversion
ABSOLUTE_ZERO_C = -273.15
CONVERSION_K_C = -273.15
CONVERSION_FACTOR_F_C = 5/9
CONVERSION_OFFSET_F_C = -32

# Temperature and Unit Input
try:
    temp_in_value = temp_value = float(input('Enter temperature:\n'))
except:
    print("Invalid input. Please enter a numeric temperature value.")
    exit()
temp_in_unit = input('Enter starting unit (C, F, K):\n').upper()
temp_out_unit = input('Enter target unit (C, F, K):\n').upper()

# Convert input temperature to Celsius
if temp_in_unit == 'F' or temp_in_unit == 'FAHRENHEIT':
    temp_value = (temp_value + CONVERSION_OFFSET_F_C) * CONVERSION_FACTOR_F_C
elif temp_in_unit == 'K' or temp_in_unit == 'KELVIN':
    temp_value = temp_value + CONVERSION_K_C
elif temp_in_unit != 'C' and temp_in_unit != 'CELSIUS':
    print("Invalid starting unit. Please enter C, F, or K.")
    exit()

# Check for temperatures below absolute zero
if temp_value < ABSOLUTE_ZERO_C:
    print("Temperature cannot be below absolute zero (-273.15 C/ -459.67 F/ 0 K).")
    exit()

# Convert from Celsius to target unit
if temp_out_unit == 'F' or temp_out_unit == 'FAHRENHEIT':
    temp_value = temp_value / CONVERSION_FACTOR_F_C - CONVERSION_OFFSET_F_C
elif temp_out_unit == 'K' or temp_out_unit == 'KELVIN':
    temp_value = temp_value - CONVERSION_K_C 
elif temp_out_unit != 'C' and temp_out_unit != 'CELSIUS':
    print("Invalid target unit. Please enter C, F, or K.")
    exit()

# Output the result
print(f"{temp_in_value} {temp_in_unit} is equal to {temp_value} {temp_out_unit}.")


