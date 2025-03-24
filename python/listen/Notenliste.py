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
import csv, sqlite3
#from tabulate import tabulate


import os
import sqlite3

# Pfad zur Datenbank (beide Tabellen werden in dieser DB gespeichert)
noten_pfad = "/Users/mirokobow/Developer/Python/BBOVG 11/Info 11/Python/noten.db"

# Prüfen, ob die Datenbank bereits existiert
if not os.path.exists(noten_pfad):
    # Verbindung zur Datenbank herstellen (erstellt die DB, falls sie nicht existiert)
    connection = sqlite3.connect(noten_pfad)
    cursor = connection.cursor()

    # Tabelle "faecher" erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faecher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    # Tabelle "noten" erstellen, mit Fremdschlüssel, der auf "faecher" verweist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fach_id INTEGER,
            note REAL,
            FOREIGN KEY (fach_id) REFERENCES faecher(id)
        )
    """)
    connection.commit()
    print("Datenbank und Tabellen wurden erstellt.")
else:
    # Verbindung zur existierenden Datenbank herstellen
    connection = sqlite3.connect(noten_pfad)
    cursor = connection.cursor()
    print(f"Die Datenbank '{noten_pfad}' wurde erfolgreich gefunden und geöffnet.")



def add_note(subject, note):
    """Fügt eine Note zu einem existierenden Fach hinzu."""
    try:
        cursor.execute("SELECT id FROM faecher WHERE name = ?", (subject,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"Fach '{subject}' existiert nicht. Bitte zuerst das Fach hinzufügen.")
            return
        
        fach_id = result[0]
        
        if not (1.0 <= note <= 6.0):
            print("Ungültige Note. Bitte eine Note zwischen 1.0 und 6.0 eingeben.")
            return
        
        cursor.execute("INSERT INTO noten (fach_id, note) VALUES (?, ?)", (fach_id, note))
        connection.commit()
        print(f"Note {note} zu '{subject}' hinzugefügt.")
    except Exception as e:
        print("Fehler beim Hinzufügen der Note:", e)

def delete_notes(subject):
    """Löscht alle Noten eines bestimmten Faches."""
    cursor.execute("SELECT id FROM faecher WHERE name = ?", (subject,))
    result = cursor.fetchone()
    if result is None:
        print(f"Fach '{subject}' wurde nicht gefunden.")
        return
    fach_id = result[0]
    cursor.execute("DELETE FROM noten WHERE fach_id = ?", (fach_id,))
    connection.commit()
    print(f"Alle Noten für '{subject}' wurden gelöscht.")


#########################################

def show_all_faecher():
    """Zeigt alle existierenden Fächer an."""
    try:
        cursor.execute("SELECT name FROM faecher")
        subjects = cursor.fetchall()
        print("######################")
        for subject in subjects:
            print(subject[0])
        print("######################")
    except Exception as e:
        print("Fehler beim Abrufen der Fächer:", e)

def show_fach(subject):
    """Zeigt alle Noten eines bestimmten Faches an."""
    cursor.execute("SELECT id FROM faecher WHERE name = ?", (subject,))
    result = cursor.fetchone()
    if result is None:
        print(f"Fach '{subject}' wurde nicht gefunden.")
        return
    fach_id = result[0]
    cursor.execute("SELECT note FROM noten WHERE fach_id = ?", (fach_id,))
    noten = cursor.fetchall()
    if not noten:
        print(f"Für '{subject}' wurden noch keine Noten eingetragen.")
    else:
        print(f"Noten für '{subject}': {[note[0] for note in noten]}")

def add_fach(subject):
    """Fügt ein neues Fach hinzu. Bei doppelter Eingabe wird eine Fehlermeldung ausgegeben."""
    try:
        cursor.execute("INSERT INTO faecher (name) VALUES (?)", (subject,))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Das Fach '{subject}' existiert bereits.")

def del_fach(subject):
    """Löscht das angebegebene Fach mit allen Noten"""

    cursor.execute("SELECT id FROM faecher WHERE name = ?", (subject,))
    result = cursor.fetchone()
    if result is None:
        print(f"Fach '{subject}' wurde nicht gefunden.")
        return
    fach_id = result[0]
    
    # Zuerst alle zugehörigen Noten löschen
    cursor.execute("DELETE FROM noten WHERE fach_id = ?", (fach_id,))
    
    # Dann das Fach selbst löschen
    cursor.execute("DELETE FROM faecher WHERE id = ?", (fach_id,))
    connection.commit()
###################

def durchschnitt():
    pass


# add_fach("Deutsch")
# add_fach("Englisch")
# add_fach("Info")
add_note("Deutsch", 1)
add_note("Deutsch", 3)
show_all_faecher()
show_fach("Deutsch")
connection.close