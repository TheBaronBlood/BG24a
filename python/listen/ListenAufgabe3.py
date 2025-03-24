# Schreiben Sie ein Programm, welches Ihre Unterrichtsfächer und die zugehörigen Noten in einer Liste 
# verwaltet.
# Das Programm soll folgendes leisten: - Speichern aller Fächer und der dazugehörigen Noten in einer einzigen Liste
# - Anzeigen der Fächer mit den Noten
# - Abfrage einzelner Fächer
# - Hinzufügen von neuen Fächern
# - Hinzufügen von Noten zu den existierenden Fächern
# - Statistische Auswertungen der Noten/Fächer
# - Absicherung von Eingabefehlern
# - Speichern/Öffnen der Noten in einer externen Datei (z.B. csv-Datei)

import os
import sqlite3
from tabulate import tabulate

noten = "Z:\Info 11\Python\noten.db"

connection = sqlite3.connect("noten.db")
cursor = connection.cursor()

if not os.path.exists(noten):
    # Erstellt eine Daten Bank mit ID , FACH, NOTEN
    cursor.execute("""             
    CREATE TABLE IF NOT EXISTS noten (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fach TEXT,
    note LIST
    );
    """)
    connection.commit()

else:
    # Verbindung zur existierenden Datenbank herstellen
    connection = sqlite3.connect(noten)
    cursor = connection.cursor()
    print(f"Die Datenbank '{noten}' wurde erfolgreich gefunden und geöffnet.")
    

# cursor.execute("""
# INSERT INTO noten (fach, note)
# VALUES ('Deutsch', 3), ('Englisch', 1), ('Mathematik', 2)
# """)
# connection.commit()


def add_Noten(fachname: str, neu_fachnoten: int):
    cursor.execute(f"""
    UPDATE noten
    SET note = {neu_fachnoten}
    WHERE fach = '{fachname}'
    """)
    connection.commit()

def del_Noten(fachname: str, del_fachnoten: int):
    cursor.execute(f"""
    DELETE FROM noten
    WHERE note = '{del_fachnoten}'
    """)

def add_Fach(neu_fachname: str, note=None):

    if note == None:
        cursor.execute("INSERT INTO noten (fach, note) VALUES (?, NULL)", (neu_fachname,))
    else:
        cursor.execute("INSERT INTO noten (fach, note) VALUES (?, ?)", (neu_fachname, note))
    
    connection.commit()

def show_database():

    cursor.execute("SELECT * FROM noten")
    daten = cursor.fetchall()

    # Spaltennamen definieren
    header = ["ID", "Fach", "Note"]
            
    return print(tabulate(daten, headers=header, tablefmt="grid"))

add_Fach("Deutsch", [1,3,4])
show_database()







# noten = [["Deutsch", 1], ["INF", 2], ["ADT", 2], ["Mathematik", 2], ["Biologie", 2]]

# def fachindex(notenliste: list, unterrichtsfach: str) -> int:
#     for i in range(len(notenliste)):
#         if unterrichtsfach == notenliste[i][0]:  
#             return i
        
# fach = input("Welches Fach: ")

# index = fachindex(noten, fach)

# print(noten[index][0])
# print(noten[index][1])

# def add_Fächer(notenliste, neufachname: str, neufachnoten: int):
#     neuesfach = []
#     neuesfach.append(neufachname)
#     neuesfach.append(neufachnoten)
#     notenliste.append(neuesfach)

# def add_noten(notenliste, fachname: str, neufachnoten: int):
#     index = fachindex(noten, fachname)
#     try:
#         fach = notenliste[index].append(neufachnoten)
#     except TypeError:
#         print("Probiere das Fach Hinzuzufügen oder Versuche es Erneut")




