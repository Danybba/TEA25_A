frage = open("Karteikartentest_Fragen.csv", "r").read().splitlines()
antwort = open("Karteikartentest_Antworten.csv", "r").read().splitlines()
lf = len(frage)
la = len(antwort)

if lf == la:
    for i in range(lf):
        print("Frage:", frage[i])
        user_input = input("Deine Antwort: ")
        if user_input.lower() == antwort[i].lower():
            print("Richtig!")
        else:
            print("Falsch! Die richtige Antwort ist:", antwort[i])