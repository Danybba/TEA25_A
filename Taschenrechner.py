zahl1 = input("Geben Sie die erste Zahl ein: ")
zahl2 = input("Geben Sie die zweite Zahl ein: ")
rechenoperator = input("Geben Sie den Rechenoperator ein (Addieren(+), Subtrahieren(-), Multiplizieren (*), Subtrahieren (/)): ")

ergebnis = 0

if rechenoperator == "+":
    ergebnis = float(zahl1) + float(zahl2)

elif rechenoperator == "-":
    ergebnis = float(zahl1) - float(zahl2)

elif rechenoperator == "*":
    ergebnis = float(zahl1) * float(zahl2)

elif rechenoperator == "/":
    try: 
         ergebnis = float(zahl1) / float(zahl2)
    except ZeroDivisionError:
         ergebnis = "Division durch Null ist nicht erlaubt."

print(f"Das Ergebnis der Berechnung ist: {ergebnis}")