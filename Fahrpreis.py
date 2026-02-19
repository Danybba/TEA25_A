ride_type = input("Wählen Sie Plus oder Comfort aus: " )

credits = int(input("Geben Sie die Anzahl der Credits ein: "))

ride_price = 0
final_price = 0

if ride_type == "Plus":
    ride_price = 20.5

if ride_type == "Comfort":
    ride_price = 37.9

else: 
    ride_price = 18.7

if credits > 0:
    final_price = ride_price - credits

else:
    final_price = ride_price

print(f"Der Fahrpreis beträgt: {ride_price} €.")
print(f"Der Endpreis nach Abzug der Credits beträgt: {final_price} €.")