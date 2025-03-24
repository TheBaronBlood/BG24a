
from tkinter import *
from tkinter import ttk
import math

def enter(event):
    ergebnisse = []

    while len(ergebnisse) < 3:
        if root.focus_get()== ".!frame.!entry":
            a = A.get()
            ergebnisse.append(a)
            print(ergebnisse, root.focus_get())
            B.focus_set()
        elif root.focus_get()== ".!frame.!entry2":
            b = B.get()
            print(ergebnisse, root.focus_get())
            ergebnisse.append(b)
            C.focus_set()
        elif C == root.focus_get():
            c = C.get()
            print(ergebnisse,  C == root.focus_get())
            ergebnisse.append(c)
    print("Hallo")
        

root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()

ttk.Label(frm, text="A:").grid(column=0, row=0)
A = ttk.Entry(frm)
A.grid(column=1, row=0)



ttk.Label(frm, text="B:").grid(column=0, row=1)
B = ttk.Entry(frm)
B.grid(column=1, row=1)



ttk.Label(frm, text="C:").grid(column=0, row=2)
C = ttk.Entry(frm)
C.grid(column=1, row=2)


Nulltellen = Label(frm, text="")

root.bind('<Return>', enter)

root.mainloop()
