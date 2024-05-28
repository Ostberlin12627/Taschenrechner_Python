import tkinter as tk
from tkinter import END

#Deklarierung der notwendigen Variablen
dezimalzahl = 0
basis = 0

#Setzt der Standartwerte der GUI
root = tk.Tk()
root.geometry("300x300")
root.configure(bg="black")

root.update_idletasks()
window_height = root.winfo_height()
font_size = window_height //10
font_style = ("Helvetica", font_size)

#Funktionen für die Tasten

def adddisplay(char):
    ausgabe.insert(END, char)

def clear_display():
    ausgabe.delete(0, END)

#Funktion für die Ergebnistaste. Sie wertet aus ein u benutzt wird und/ oder gibt den Wert zurück
def result():
    try:
        inhalt = ausgabe.get()
        if "u" in inhalt and any(op in inhalt for op in "+-*/()"):
            raise ValueError("Error")
        elif "u" in inhalt:
            dezimalzahl = int(inhalt.split("u")[0])
            basis = int(inhalt.split("u")[1])
            ende = str(dezimal_zu_anderer_basis(dezimalzahl, basis))
            ausgabe.delete(0, END)
            ausgabe.insert(0, ende.strip())
        else:
            gleich = eval(ausgabe.get())
            ausgabe.delete(0, END)
            ausgabe.insert(0, str(gleich))
    except Exception as e:
        ausgabe.delete(0, END)
        ausgabe.insert(0, str(e))

#Funktioin zum umwandeln einer Dezimalzahl in ein anders Zahlensystem
def dezimal_zu_anderer_basis(dezimalzahl, basis):
    ascii = []
    while dezimalzahl > 0:
        rechnung = int(((dezimalzahl / basis) - int(dezimalzahl / basis)) * basis)
        if rechnung >= 10:
            ascii.append(chr(rechnung + 55))
        else:
            ascii.append(str(rechnung))
        dezimalzahl = int(dezimalzahl / basis)
    ascii.reverse()
    ergebnis = "".join(ascii)
    return ergebnis

# Positionieren der Tasten
ausgabe = tk.Entry(root, font=font_style)
ausgabe.grid(row=0, column=0, rowspan=2, columnspan=5, padx=2, pady=2, sticky="nsew")  

delete_button = tk.Button(root, text="DEL", font=font_style, bg="#000000", fg="#FFFFFF", command=lambda:clear_display())
delete_button.grid(row=5, column=3, columnspan=2, padx=1, pady=1, sticky="nsew")

result_button = tk.Button(root, text="=", font=font_style, bg="#000000", fg="#FFFFFF", command=lambda: result())
result_button.grid(row=6, column=0, columnspan=5, padx=1, pady=1, sticky="nsew")


buttonlabels = ["7", "8", "9", "(", ")", "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", ".", "0","u"]

for i, label in enumerate(buttonlabels):
    if label == "DEL":
        button = tk.Button(root, text=label, font=font_style,bg="#000000", fg="#FFFFFF", command=clear_display)
    else:
        button = tk.Button(root, text=label,font=font_style, bg="#000000", fg="#FFFFFF", command=lambda l=label: adddisplay(l))
    
    row = (i // 5) + 2  
    column = i % 5
    button.grid(row=row, column=column, padx=1, pady=1, sticky="nsew")

#Sorgt dafür das die Tasten Dynamisch werden
for column in range(5):
    root.columnconfigure(column, weight=1)  
for row in range(7):
    root.rowconfigure(row, weight=1)  

root.mainloop()
