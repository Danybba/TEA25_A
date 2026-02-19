heart_rate = int(input("Geben Sie IHRE Herzfrequwnz ein: "))
too_low = heart_rate < 60
too_high = heart_rate > 100
good_heart_rate = not too_low and not too_high
print("Herzfrequenz Status:", "zu niedrig" if too_low else "zu hoch" if too_high else "in Ordnung")