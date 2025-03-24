Eingabe = None
werte = [3,8,7,1,3,2,0]

# while Eingabe != "0":
#     Eingabe = input("Gebe eine Zahl ein: ")
#     liste.append(Eingabe)

def esortieren(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i] < liste[j]:
                print(liste)
                liste[i], liste[j] = liste[j], liste[i] 
                print(liste)
    return liste



def sortieren(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-i-1):
            if liste[j] > liste[j+1]:
                print(f"i:{i} j:{j}")
                liste[j], liste[j+1] = liste[j+1], liste[j] 
                print(liste)
    return liste



print(sortieren(werte))
print("min:",sortieren(werte)[0], "max:",sortieren(werte)[-1])