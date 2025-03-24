import os

win = False
symbole = ["X", "O"] # Deklariert welche Symbole Verwendet werden
O = [] # Ort für die Seicherung der Position des Zeichens
X = [] # Ort für die Seicherung der Position des Zeichens
g = True
pos = {1: " ", 2: " ", 3: " ",   # Positionen des Feldes 
       4: " ", 5: " ", 6: " ",   # mit den dazugehörigem 
       7: " ", 8: " ", 9: " "}   # gesetzen zeichen

wincon = [
    # Horizontale Gewinnbedingungen
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    
    # Vertikale Gewinnbedingungen
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    
    # Diagonale Gewinnbedingungen
    [1, 5, 9], [3, 5, 7]
]


def check_win(con, lst):
    return any(set(condition).issubset(lst) for condition in con) # Fragt ob con in lst iwie vorhanden ist
# Gibt das Spielfeld aus


while not win:
    for s in range(1,3):
            os.system("cls") # cleart das Fenster
            for row in range(3):  # 3 Zeilen
                for col in range(3):  # 3 Spalten pro Zeile
                    print(f"[{pos[col + 1 + row *3]}]", end="")  # Bleibt in der gleichen Zeile
                print()  # Neue Zeile nach jeder Reihe
            
            for p,j in zip(pos.values(), range(1,10)):
                if p == symbole[0]:
                    X.append(j)
                elif p == symbole[1]:
                    O.append(j)
            # print(f"O: {O}")
            # print(f"X: {X}")
            
            
            
            if check_win(wincon, O):
                win = True
                break  # Beendet die Schleife sofort, wenn X gewonnen hat

            if check_win(wincon, X):
                win = True
                break  # Beendet die Schleife sofort, wenn X gewonnen hat
            
            O = []  # Cleart die liste damit nicht sich auf addiert
            X = []  # Cleart die liste damit nicht sich auf addiert
            
          
            while g:
                eingabe = int(input(f"Spieler {s}: "))
                    
                if pos[eingabe] != "X" and pos[eingabe] != "O":
                    pos[eingabe] = symbole[s-1]
                    g = False
                    continue
                os.system("cls")
                for row in range(3):  # 3 Zeilen
                    for col in range(3):  # 3 Spalten pro Zeile
                        print(f"[{pos[col + 1 + row *3]}]", end=" ")  # Bleibt in der gleichen Zeile
                    print()  # Neue Zeile nach jeder Reihe
            g = True
                
                    
            


            



print(f"Spieler {s} hat gewonnen")
        

