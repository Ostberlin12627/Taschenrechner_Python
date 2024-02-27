from tkinter import *
from tkinter import font
dezimalzahl = 0
basis = 0
#erstellen des Fensters und Festsetzen von schriftgröße und Art
root = Tk()
root.configure(bg="black",borderwidth=10, relief="sunken")

font_general = font.Font(size=20, family="Arial")

#Funktion um etwas einzugeben
def adddisplay(char):
    ausgabe.insert(END,char)

#Funktion zum Löschen der Anzeige
def clear_ausgabe():
    ausgabe.delete(0, END)

#Funktion um das ergebnis auszugeben. wenn ein "u" vorhanden ist, wird die Umrechnung ausgeführt.
#Sollten ein Kombination aus u und einem anderem Sondernzeichen bestehen so wird Error auf dem Display angezeigt.
def ausrechnen():
    try:
        inhalt = ausgabe.get()
        if "u" in inhalt and any(op in inhalt for op in "+-*/()"):
            raise ValueError("Error")
        elif "u" in inhalt:
            dezimalzahl = int(inhalt.split("u")[0])
            basis =int(inhalt.split("u")[1])
            ende = str(dezimal_zu_anderer_basis(dezimalzahl, basis))
            ausgabe.delete(0, END)
            ausgabe.insert(0, ende.strip())
        else:
            gleich = eval(ausgabe.get())
            ausgabe.delete(0, END)
            ausgabe.insert(0,str(gleich))
    except Exception as e:
        ausgabe.delete(0, END)
        ausgabe.insert(0, str(e))

#Funktion zum Umrechnen in andere in 33 Zahlensystem
def dezimal_zu_anderer_basis(dezimalzahl,basis):
    ascii = []
    while dezimalzahl >0:
        rechnung = int(((dezimalzahl / basis) - int(dezimalzahl / basis)) * basis)
        #              (     (35 / 2)         -     (34 /2)     )         *   2
        if rechnung >10:
            ascii.append(chr(rechnung + 55))
        else:
            ascii.append(str(rechnung))
        dezimalzahl = int(dezimalzahl / basis)
    ascii.reverse()
    ergebnis = "".join(ascii)
    return ergebnis

#Ziffern 0-9
taste1 = Button(root, text = "1",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("1"))
taste2 = Button(root, text = "2",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("2"))
taste3 = Button(root, text = "3",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("3"))
taste4 = Button(root, text = "4",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("4"))
taste5 = Button(root, text = "5",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("5"))
taste6 = Button(root, text = "6",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("6"))
taste7 = Button(root, text = "7",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("7"))
taste8 = Button(root, text = "8",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("8"))
taste9 = Button(root, text = "9",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("9"))
taste0 = Button(root, text = "0",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("0"))

#Grundrechenarten
taste_addition = Button (root, text = "+",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("+"))
taste_subtraktion = Button(root, text = "-",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("-"))
taste_division = Button(root, text = ":",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("/"))
taste_multiplikation = Button(root, text = "X",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("*"))

#Ergebnistaste und umrechnung in andere Basis
taste_umrechnung = Button(root, text = "U",bg="#000000",fg="#FFFFFF",font=font_general, command=lambda: adddisplay("u"))
taste_gleich = Button(root,text ="=",bg="#000000", fg="#FFFFFF",font=font_general,command=ausrechnen)

#Punkt und Anzeigefeld löschen
taste_punkt = Button(root, text = ".",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("."))
taste_löschen = Button(root,text ="Del",bg="#000000",fg="#FFFFFF",font=font_general,command=clear_ausgabe)
taste_klammaauf = Button(root,text ="(",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay("("))
taste_klammazu = Button(root,text =")",bg="#000000",fg="#FFFFFF",font=font_general,command=lambda:adddisplay(")"))

#Aufbau des GUI richtet und einteilung des GUI´s
#erstellen des Ausgabefensters
ausgabe = Entry(root, font=font_general)
ausgabe.grid(row=0, column=0,columnspan=5, sticky="nswe")

#Tasten der ersten Reihe
taste7.grid(row=1, column=0, sticky="nswe")
taste8.grid(row=1, column=1, sticky="nswe")
taste9.grid(row=1, column=2, sticky="nswe")
taste_multiplikation.grid(row=1,column=3, sticky="nswe")
taste_division.grid(row=1, column=4, sticky="nswe")

#Tasten der zweiten Reihe
taste4.grid(row=2, column=0, sticky="nswe")
taste5.grid(row=2, column=1, sticky="nswe")
taste6.grid(row=2, column=2, sticky="nswe")
taste_subtraktion.grid(row=2, column=3, sticky="nswe")
taste_addition.grid(row=2, column=4, sticky="nswe")

#Tasten der dritten reihe
taste1.grid(row=3, column=0, sticky="nswe")
taste2.grid(row=3, column=1, sticky="nswe")
taste3.grid(row=3, column=2, sticky="nswe")
taste_umrechnung.grid(row=3, column=3, sticky="nswe")
taste_gleich.grid(row=3, column=4, sticky="nswe")

#Tasten der 4ten Reihe
taste_punkt.grid(row=4, column=0, sticky="nswe")
taste0.grid(row=4, column=1, sticky="nswe")
taste_löschen.grid(row=4, column=4, sticky="nswe")
taste_klammaauf.grid(row=4, column=2, sticky="nswe")
taste_klammazu.grid(row=4, column=3, sticky="nswe")

#Anpassen der Größe an das Fenster
for column in range(5):
    root.columnconfigure(column, weight=2)
for row in range(6):
    root.rowconfigure(row, weight=2)
root.mainloop()

print(dezimalzahl)