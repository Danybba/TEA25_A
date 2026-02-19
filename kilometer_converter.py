"Wir wollen Meilen in Kilometer umwandeln. "
"1 Meile entspricht 1.60934 Kilometer. "
"Schreibe ein Programm"

MILE_TO_KILOMETER_FACTOR = 1.60934

input_miles = int(input("Geben Sie die Anzahl der Meilen ein: "))

kilometers = input_miles * MILE_TO_KILOMETER_FACTOR
print("Die Anzahl der Kilometer beträgt:", kilometers, "km"