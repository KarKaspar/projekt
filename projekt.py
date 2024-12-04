from tkinter import *
from tkinter import ttk

def caesar_krüpti(tekst, nihe=3): #defineerib funktsiooni caesar_krüpti, mis võtab argumendiks teksti ja nihke, mille väärtuseks on 3, ehk nihutab tähti 3 võrra paremale
    krüpteeritud_tekst = "" #tekst mida krüpteerida
    for täht in tekst:  #iga tähe kohta  tekstis
        if täht.isalpha():
            nihe_suurus = 65 if täht.isupper() else 97 # Määrab ASCII algväärtuse: 65 suurte tähtede jaoks, 97 väikeste tähtede jaoks
            ascii_väärtus = ord(täht) # Teisendab tähe ASCII väärtuseks
            nihutatud_positsioon = (ascii_väärtus + nihe - nihe_suurus) % 26 # Arvutab nihutatud tähe positsiooni tähestikus (0-25)
            nihutatud_ascii = nihutatud_positsioon + nihe_suurus # Arvutab nihutatud tähe ASCII väärtuse
            nihutatud_täht = chr(nihutatud_ascii) # Teisendab ASCII väärtuse tagasi täheks
            krüpteeritud_tekst += nihutatud_täht # Lisab nihutatud tähe krüpteeritud teksti
        else:
            krüpteeritud_tekst += täht
    return krüpteeritud_tekst #tagastab krüpteeritud teksti

def caesar_dekrüpti(tekst, nihe=3): #defineerib funktsiooni caesar_dekrüpti, mis võtab argumendiks teksti ja nihke (3 võrra tagasi vasakule)
    return caesar_krüpti(tekst, -nihe) #tagastab dekrüpteeritud teksti

def main(): #defineerib funktsiooni main
    while True: #kui tõene
        valik = input("Vali toiming: (1) Krüpteeri (2) Dekrüpteeri (3) Välju: ") #küsib kasutajalt valikut
        if valik == '1': #kui valik on 1 kuvatakse järgnev tekst
            tekst = input("Sisesta tekst krüpteerimiseks: ")
            if not tekst.isalpha():
                print("Viga: Sisestada võib ainult tähti. Numbrid ja sümbolid ei ole lubatud. Proovi uuesti")
                continue #kui sisestatakse numbrid või sümbolid, siis veateade ja alustatakse ueusti
            print("Krüpteeritud tekst:", caesar_krüpti(tekst)) #kui sisetsatud õiged väärtused kuvatakse krüpteeritud tekst
        elif valik == '2': #kui valik on 2 kuvatakse järgnev tekst
            tekst = input("Sisesta tekst dekrüpteerimiseks: ")
            if not tekst.isalpha(): #kui pole sisestatud ainult tähti, siis veateade ja uuesti
                print("Viga: Sisestada võib ainult tähti. Numbrid ja sümbolid ei ole lubatud. Proovi uuesti")
                continue
            print("Dekrüpteeritud tekst:", caesar_dekrüpti(tekst))
        elif valik == '3': #kui valik on 3, siis programm lõpetab töö
            break
        else:
            print("Lubatud on sisestada ainult tähti. Proovi uuesti.") 

    main() #käivitab funktsiooni main

def krüpteerminie():
    if valik.get() == "Tekst":
        user = nimi.get()
        nimi.delete(0, END)
        nimi.insert(0, caesar_krüpti(user))
    else:
        # fail
        user = nimi.get()
        vastus.config(text=caesar_krüpti(user))

def dekrüpteerminie():
    if valik.get() == "Tekst":
        user = nimi.get()
        nimi.delete(0, END)
        nimi.insert(0, caesar_dekrüpti(user))
    else:
        # fail
        user = nimi.get()
        vastus.config(text=caesar_dekrüpti(user))

#aken
aken = Tk()
aken.title("LOENG 5")
aken.geometry("450x300")

#stiil
s = ttk.Style()
s.configure('Danger.TFrame',
            borderwidth=5,
            relief='raised')
#raam                      
raam = ttk.Frame(aken,
                 width=450,
                 height=300,
                 style='Danger.TFrame').grid()

# tekst
silt = ttk.Label(raam, text="Tekst:")
silt.place(x=5, y=100)

# tekst
vastus = ttk.Label(raam, text="")
vastus.place(x=50, y=50)

# sisestatav kast
nimi = ttk.Entry(raam)
nimi.insert(0, "Krupteeritav voi dekrupteeritav tekst siia")
nimi.place(x=70, y=100, width=250)

# loome nupu
nupp = ttk.Button(raam, text="Krüpteeri", command=krüpteerminie)  
nupp.place(x=70, y=240)
nupp = ttk.Button(raam, text="Dekrüpteeri", command=dekrüpteerminie)  
nupp.place(x=160, y=240)

# Raadionupp
def val(): 
    print(valik.get())

valik = StringVar(value="Tekst")

Tekst = ttk.Radiobutton(raam, text="Tekst",
                         command =val,
                         variable=valik,
                         value="Tekst")
Tekst.place(x=70, y=130, width=150)

Fail = ttk.Radiobutton(raam,
                       text="Fail",
                       command =val,
                       variable=valik,
                       value="Fail")
Fail.place(x=70, y=160, width=150)

aken.mainloop()
