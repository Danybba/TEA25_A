time = input("Geben sie eine Uhrzeit ein: (0-23) ")
time = (0-23)
if int(time) < 12:
    print("Guten Morgen.")
if int(time) >= 12 and int(time) < 18:
    print("Guten Tag.")
if int(time) >= 18 and int(time) <= 20:
    print("Guten Abend.")
else:
    print("Gute Nacht.")