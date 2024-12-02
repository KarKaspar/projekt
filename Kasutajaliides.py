from tkinter import *
from tkinter import ttk


def krüpteerminie():
    if valik.get() == "Tekst":
        user = nimi.get()
        print(user)
    else:
        # fail
        print("a")

def dekrüpteerminie():
    if valik.get() == "Tekst":
        user = nimi.get()
        print(user)
    else:
        # fail
        print("b")

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

# sisestatav kast
nimi = ttk.Entry(raam)
nimi.insert(0, "Krüpteeritav või dekrüpteeritav text siia")
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
