# entered_pin = int(input("Geben Sie Ihren PIN ein: "))
# expected_pin = 4567

# print(entered_pin == expected_pin)

# print(entered_pin, "not correct:")

# ' formated printing'
# print(f"{entered_pin} is not correct:")

# # print(f" Deine eingegeben Zahl {zahl} ist nicht korrekt. Bitte versuche es erneut.")

# age = int(input("Geben Sie Ihr Alter ein: "))

# driver_license = bool(int(input("Haben Sie einen Führerschein? (1 für Ja, 0 für Nein): ")))

# drunk = bool(int(input("Sind Sie betrunken? (1 für Ja, 0 für Nein): ")))

# insurance = bool(int(input("Haben Sie eine Versicherung? (1 für Ja, 0 für Nein): ")))

# if (age >= 18) and (driver_license == True) and (drunk == False) and (insurance == True):
#     print("Can drive!")
# else:   
#     print("Cannot drive!")




# greet = False

# if greet:
#     print("Hallo Welt")
#     print("Hallo Welt")

# hour = int(input("Geben Sie die aktuelle Stunde ein (0-23): "))

# if hour < 12:
#     print("Guten Morgen!")
# elif hour < 18:
#     print("Guten Tag!")
# elif hour < 22:
#     print("Guten Abend!")
# else:
#     print("Gute Nacht!")

final_score = int(input("Geben Sie Ihre Endpunktzahl ein: "))
average_score = int(input("Geben Sie Ihre Durchschnittspunktzahl ein: "))

if (final_score >= 90) or (average_score >= 85):
    print("Bestanden!")
else:
    print("Nicht bestanden!")