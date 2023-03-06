import random
import sys
import os
import subprocess

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

message = []
cipher = []
choice = 0
data = []
dec_message_arr = []
dec_message_gui = ""

primes = []
p = 0
q = 0

tot = 0

n = 0
e = 0
d = 0


FermatPrimes = [17, 257, 65537, 42944967297]


def AllPrimesInRange():
    min = 100
    max = 200

    for i in range(min, max):
        for x in range(2, i):
            if (i % x == 0):
                break
        else:
            primes.append(i)


def Define_p_q():
    global p, q
    while True:
        x = random.randint(0, (len(primes))-1)
        y = random.randint(0, (len(primes))-1)
        p = primes[x]
        q = primes[y]
        if p != q:
            break

    print("p: ", p, "q: ", q)


def DefinePublic():
    global n, e
    n = p * q
    print("n:", n)

    while True:
        x = random.randint(0, (len(FermatPrimes))-1)
        e = FermatPrimes[x]
        if e < tot:
            break

    print("e: ", e)


def CalculateTot():
    global p, q, tot

    x = p - 1
    y = q - 1
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            tot = greater
            break
        greater += 1

    print("tot: ", tot)


def DefinePrivate():
    global d

    for x in range(1, tot):
        if (((e % tot) * (x % tot)) % tot == 1):
            break
    d = x
    print("d: ", d)


current_window = None


def OnSubmitTxtDatoteka():
    global enkrbes, n, d, e
    global cipher

    # clean message and cipher (message can't be global)
    message = []
    cipher = []

    AllPrimesInRange()
    Define_p_q()
    CalculateTot()
    DefinePublic()
    DefinePrivate()

    message = Text_box.get("1.0", "end-1c")

    for i in message:
        cipher.append((ord(i) ** e) % n)

    # writing to file
    f = open("encrypted.txt", "w")
    f.write(str(cipher))
    f.close()

    subprocess.run(["messageFormat.bat"], shell=True)

    Label(enkrbes, text="Sporočilo je bilo enkriptirano s ključem:", font=("Arial", 10, "bold")).grid(
        row=3, column=0)
    Label(enkrbes, text="n:").grid(row=4, column=0, padx=10, pady=10)
    Label(enkrbes, text="e:").grid(row=5, column=0, padx=10, pady=10)

    n_label = Label(enkrbes, text=n, font=("Arial", 10, "bold"),
                    foreground="#655DBB")
    n_label.grid(row=4, column=1, padx=10, pady=10)

    e_label = Label(enkrbes, text=e, font=("Arial", 10, "bold"),
                    foreground="#655DBB")
    e_label.grid(row=5, column=1, padx=10, pady=10)

    Label(enkrbes, text="Za dekriptiranje uporabi:", font=("Arial", 10, "bold")).grid(
        row=6, column=0)
    Label(enkrbes, text="n:").grid(row=7, column=0, padx=10, pady=10)
    Label(enkrbes, text="d:").grid(row=8, column=0, padx=10, pady=10)

    n_label.config(cursor='xterm')

    n_label = Label(enkrbes, text=n, font=("Arial", 10, "bold"),
                    foreground="#655DBB")
    n_label.grid(row=7, column=1, padx=10, pady=10)

    d_label = Label(enkrbes, text=d, font=("Arial", 10, "bold"),
                    foreground="#655DBB")
    d_label.grid(row=8, column=1, padx=10, pady=10)

    n_label.config(cursor='xterm')
    e_label.config(cursor='xterm')
    d_label.config(cursor='xterm')


def OnSubmitDatotekaBesedilo():
    global dec_message_gui
    global dekrbes
    global message, cipher, n, d

    n = int(n_gui.get("1.0", "end-1c"))
    d = int(d_gui.get("1.0", "end-1c"))

    print("\nOdpiranje .txt datoteke... \n")
    f = open("encrypted.txt", "r")
    cipher = f.read().split()
    f.close()

    for i in cipher:
        message.append((int(i) ** d) % n)

    for i in message:
        dec_message_arr.append(chr(i))

    dec_message_gui = ''.join(dec_message_arr)

    Label(dekrbes, text="Dekriptirano sporočilo:", font=('Arial', 10)).grid(
        row=4, column=1, padx=5, pady=5)

    Label(dekrbes, text=dec_message_gui, font=('Arial', 15, "bold"), foreground="#655DBB").grid(
        row=5, column=1, padx=5, pady=5)


def EnkrBesVDatoteko():
    global Text_box
    global enkrbes

    enkrbes = tk.Tk()

    enkrbes.title("Enkriptiranje besedila")
    # enkrbes.geometry('400x400')

    Label(enkrbes, text="Vpišite sporočilo za enkripcijo:").grid(
        row=0, column=0)

    # create an input box and add it to the enkrbes
    Text_box = tk.Text(enkrbes, width=50, height=5,
                       font=('Arial, 12'))

    Text_box.grid(row=1, column=0)

    # create a button to submit the input
    submit_button = tk.Button(enkrbes, text="Submit",
                              command=OnSubmitTxtDatoteka)

    submit_button.grid(row=2, column=0)

    # Set the protocol to handle window closing
    enkrbes.protocol("WM_DELETE_WINDOW", lambda: close_window(enkrbes))

    return enkrbes


def DekrBesIzDatoteke():

    global n_gui
    global d_gui
    global dekrbes
    dekrbes = tk.Tk()

    dekrbes.title("Dekriptiranje besedila")
    # dekrbes.geometry('400x400')
    # create an input box and add it to the enkrbes

    Label(dekrbes, text="Vnesite zasebni ključ").grid(
        row=0, column=0, padx=10, pady=10)

    n_value = Label(dekrbes, text="n = ")
    n_value.grid(row=1, column=0, pady=(0, 5), padx=5)

    d_value = Label(dekrbes, text="d = ")
    d_value.grid(row=2, column=0, pady=(0, 15), padx=5)

    n_gui = tk.Text(dekrbes, font=('Arial, 10'), width=15, height=1)
    n_gui.grid(row=1, column=1, pady=(0, 5), padx=5)

    d_gui = tk.Text(dekrbes, font=('Arial, 10'), width=15, height=1)
    d_gui.grid(row=2, column=1, pady=(0, 15), padx=5)

    # create a button to submit the input
    submit_button = tk.Button(dekrbes, text="Potrdi",
                              command=OnSubmitDatotekaBesedilo)
    submit_button.grid(row=1, column=2, padx=10, pady=10)

    # Set the protocol to handle window closing
    dekrbes.protocol("WM_DELETE_WINDOW", lambda: close_window(dekrbes))

    return dekrbes


def PoljubnoDekr():
    PoljubnoDekr = Tk()

    # Set the protocol to handle window closing
    PoljubnoDekr.protocol("WM_DELETE_WINDOW",
                          lambda: close_window(PoljubnoDekr))

    PoljubnoDekr.title("Poljubno dekriptiranje")
    PoljubnoDekr.geometry('400x400')

    c = Label(PoljubnoDekr, text="Poljubno dekriptiranje").pack()

    return PoljubnoDekr


def DekrPoljubneDat():
    DekrPoljubneDat = Tk()

    # Set the protocol to handle window closing
    DekrPoljubneDat.protocol(
        "WM_DELETE_WINDOW", lambda: close_window(DekrPoljubneDat))

    DekrPoljubneDat.title("Dekriptiranje poljubne datoteke")
    DekrPoljubneDat.geometry('400x400')

    d = Label(DekrPoljubneDat, text="Dekriptiranje poljubne datoteke").pack()

    return DekrPoljubneDat


def windowChoice():
    global current_window
    if current_window:
        current_window.destroy()
    if v.get() == 1:
        current_window = EnkrBesVDatoteko()
    elif v.get() == 2:
        current_window = DekrBesIzDatoteke()
    elif v.get() == 3:
        current_window = PoljubnoDekr()
    elif v.get() == 4:
        current_window = DekrPoljubneDat()


def close_window(window):
    global current_window
    current_window = None
    window.destroy()


if __name__ == '__main__':

    root = Tk()

    root.title("RSA kriptiranje")
    root.geometry('700x700')

    v = IntVar()

    style = Style(root)
    style.configure("TRadiobutton",
                    foreground="black", font=("arial", 15, "bold"))

    # Dictionary to create multiple buttons
    values = {"Enkriptiraj besedilo v datoteko": 1,
              "Dekriptiraj besedilo iz datoteke": 2,
              "Poljubno dektriptiranje": 3,
              "Dekriptiranje poljubne datoteke": 4}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(root, text=text, variable=v,
                    value=value, command=windowChoice).pack(side=TOP, ipady=10)

    root.mainloop()

    # while True:
    #     choice = 0
    #     print("Izberite moznost:\n")
    #     print("1-Kriptiranje -> encrypted.txt\n")
    #     print("2-encrypted.txt -> Dekriptiranje\n")
    #     print("3-Poljubno dekriptiranje\n")
    #     print("4-Kriptiranje poljubne .txt datoteke -> encrypted.txt - in development\n")
    #     choice = int(input("Moznost: "))

    #    if choice == 1:

    #        print("Računanje vrednosti...")

    #        AllPrimesInRange()
    #        Define_p_q()
    #        CalculateTot()
    #        DefinePublic()
    #        DefinePrivate()

    #        message = input("\nVnesite sporočilo: \n")
    #        break
    #    elif choice == 2:
    #        print("\nVnesite zasebni ključ: ")
    #        n = int(input("n: "))
    #        d = int(input("d: "))

    #        print("\nOdpiranje .txt datoteke... \n")
    #        f = open("encrypted.txt", "r")
    #        cipher = f.read().split()

    #        f.close()
    #        break
    #    elif choice == 3:
    #        print("\nVnesite zasebni ključ: ")
    #        n = int(input("n: "))
    #        d = int(input("d: "))

    #        cipher = input("\nVnesite enrkiptirano sporočilo: ").split()
    #        break
    #    elif choice == 4:
    #        print("Računanje vrednosti...")

    #        AllPrimesInRange()
    #        Define_p_q()
    #        CalculateTot()
    #        DefinePublic()
    #        DefinePrivate()

    #        print("\nOdpiranje datoteke...")

    #        f = open("message.txt", "r")
    #        message = f.read()

    #        f.close()
    #        break
    #    else:
    #        print("----------------Nepravilno!------------")

    # if choice == 1 or choice == 4:

    #    for i in message:
    #        cipher.append((ord(i) ** e) % n)

    #    # writing to file
    #    f = open("encrypted.txt", "w")
    #    f.write(str(cipher))
    #    f.close()

    #    subprocess.run(["messageFormat.sh"], shell=True)
    #    print("\nEnkripcija končana, glej datoteko \"encrypted.txt\"\n")
    #    print("\nPritisni tipko ENTER za izhod...")
    #    input()

    # elif choice == 2 or choice == 3:

    #    for i in cipher:
    #        message.append((int(i) ** d) % n)

    #    print("\nDekodirano sporočilo: ")
    #    for i in message:
    #        print(chr(i), end='')
    #    print("\nPritisni tipko ENTER za izhod...")
    #    input()
