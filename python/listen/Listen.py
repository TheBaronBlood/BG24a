# 03.03.2025

# listen
werte = [] 
# eing = input("Füge etwas der Liste Hinzu: ")
# werte.append(eing) # Fügt einer liste was hinzu
# werte.append(input("Füge noch etwas die Liste Hinzu: "))
# werte.append(input("Füge noch etwas die Liste Hinzu: "))

for i in range(1,8):
    # werte.append(input("Füge etwas hinzu: "))
    werte.append(i**i)

print(werte)
#print(werte[0]) # Inhalte einer liste werden mit dem Inxdes aufgerufen

# for i in range(len(werte)):
#     print(werte[i])
summe = 0
def Arithmetischer_Mittelwert(values: list) -> int:
    try:
        for i in range(len(values)):    # zählt i auf solange wie viele Werte in der List sind
            summe = summe + values[i]        # Summiert die werte
    except TypeError:
        print("Es ist keine Liste als Wert hinzugefügt worden")

    return summe/(len(values))    # Teilt die Summe durch die Anzahl und gibt sie Zurück

print(Arithmetischer_Mittelwert([3,5,4,1,2]))

# werte.pop() # Entfernt den Letzten wert
# print(werte)
# werte.pop(2) # Entfernt den 2 also 27 wert
# print(werte)