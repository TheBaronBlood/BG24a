import math
import matplotlib.pyplot as plt
import numpy as np

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

 

def plotten(a,b,c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Verschiebe die x- und y-Achsen auf die 0-Position
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # Verberge die oberen und rechten Rahmenlinien
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Setze Gitterlinien für eine bessere Übersicht
    ax.grid(True)

    # Verschiebe die x- und y-Achsenticks auf die gegenüberliegenden Seiten der Achsen
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratische Funktion mit zentrierten Achsen')

    plt.show()


def nullstellen(p,q,D):
    x1 = -(p/2) + math.sqrt(D)
    x2 = -(p/2) - math.sqrt(D)
    if x1 == x2:
        print(x1)
    else:
        print(x1)
        print(x2)



if A == 0 :
    if B == 0:
        if C == 0:
            print("Unendlich Viele Lösungen")
        else:
            print("Gerade / Konstante")
            print(C)
            exit
    else:
        print("Lineare Gleichung")
        print(f"{B}x{C}")
else:
    p = B/A
    q = C/A
    D = (p/2)**2-q
    if D < 0:
        print("Es gibt keine Lösung")
    elif D == 0:
        print("Eine Lösung")
        nullstellen(p,q,D)
        plotten(A,B,C)
    elif D > 0:
        print("Zwei Lösungen")
        nullstellen(p,q,D)
        plotten(A,B,C)
    




