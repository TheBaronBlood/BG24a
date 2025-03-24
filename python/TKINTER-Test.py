from tkinter import *
from tkinter import ttk
import math

def enter(event):
    ergebnisse = []

    while len(ergebnisse) < 3:
        if e1 == root.focus_get():
            a = float(e1.get())
            ergebnisse.append(a)
            print(ergebnisse)
            e2.focus_set()
        elif e2 == root.focus_get():
            b = float(e2.get())
            print(ergebnisse)
            ergebnisse.append(b)
            e2.focus_set()
        elif e3 == root.focus_get():
            c = float(e3.get())
            print(ergebnisse)
            ergebnisse.append(c)

    def nullstellenberechnen(p, q, D):
        x1 = -(p/2) + math.sqrt(D)
        x2 = -(p/2) - math.sqrt(D)
        if x1 == x2:
            Nulltellen.config(text=x1)
        else:
            Nulltellen.config(text=f"x1: {x1} | x2: {x2}")

    if a == 0:
        if b == 0:
            if c == 0:
                Nulltellen.config(text="Unendlich Viele Lösungen")
            else:
                Nulltellen.config(text="Gerade / Konstante")
                Nulltellen.config(text=c)
                exit
        else:
            Nulltellen.config(text="Lineare Gleichung")
            Nulltellen.config(text=f"{b}x{c}")
    else:
        p = b/a
        q = c/a
        D = (p/2)**2 - q
        if D < 0:
            print("Es gibt keine Lösung")
        elif D == 0:
            Nulltellen.config(text="Es gibt eine Lösung")
            nullstellenberechnen(p, q, D)
        elif D > 0:
            Nulltellen.config(text="Zwei Lösungen")
            nullstellenberechnen(p, q, D)

root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()

ttk.Label(frm, text="A:").grid(column=0, row=0)
e1 = ttk.Entry(frm)
e1.grid(column=1, row=0)
ergebnis_a = Label(frm, text="")

ttk.Label(frm, text="B:").grid(column=0, row=1)
e2 = ttk.Entry(frm)
e2.grid(column=1, row=1)
ergebnis_b = Label(frm, text="")

ttk.Label(frm, text="C:").grid(column=0, row=2)
e3 = ttk.Entry(frm)
e3.grid(column=1, row=2)
ergebnis_b = Label(frm, text="")

Nulltellen = Label(frm, text="")

root.bind('<Return>', enter)

root.mainloop()
