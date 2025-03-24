

def Arithmetischer_Mittelwert(values: list) -> int:
    try:    # Probirt ob das Zählen geht und macht es
        summe = 0
        for i in range(len(values)):    # zählt i auf solange wie viele Werte in der List sind
            summe += values[i]        # Summiert die werte
        print(summe)
    except TypeError: # Falls es nicht geht gibt er einen Error
        print("Es ist keine Liste als Wert hinzugefügt worden")

    return summe/(len(values))

Noten = {"Deutsch": [3,5,4,1,2],
         "Englisch": [1,3,5,2],
         "Mathematik": [1,2,3,3,1],
         "Informatik": [1,1,1,2,1]}

while True:
    ein = input("Für welches Fach möchtest du deine Noten wissen ?  :")
    print(Noten[ein])
    option = input("Möchtest du den Durchschnitt wissen ? y/n  :")
    if option.lower() == "y":
        print(Arithmetischer_Mittelwert(Noten[ein]))
