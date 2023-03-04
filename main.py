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


# # def EnkrBesVDatoteko():
# #     enkrbes = Tk()

# #     enkrbes.title("Enkriptiranje besedila")
# #     enkrbes.geometry('400x400')

# #     a = Label(enkrbes, text="Enkriptiranje besedila").pack()

# #     enkrbes.mainloop()


# # def DekrBesIzDatoteke():

# #     dekrbes = Tk()

# #     dekrbes.title("Dekriptiranje besedila")
# #     dekrbes.geometry('400x400')

# #     b = Label(dekrbes, text="Dekriptiranje besedila").pack()

# #     dekrbes.mainloop()


# # def windowChoice():
# #     if v.get() == 1:
# #         EnkrBesVDatoteko()
# #     elif v.get() == 2:
# #         DekrBesIzDatoteke()


current_window = None


def EnkrBesVDatoteko():
    enkrbes = Tk()

    enkrbes.title("Enkriptiranje besedila")
    enkrbes.geometry('400x400')

    a = Label(enkrbes, text="Enkriptiranje besedila").pack()

    return enkrbes


def DekrBesIzDatoteke():

    dekrbes = Tk()

    dekrbes.title("Dekriptiranje besedila")
    dekrbes.geometry('400x400')

    b = Label(dekrbes, text="Dekriptiranje besedila").pack()

    return dekrbes


def windowChoice():
    global current_window
    if current_window:
        current_window.destroy()
    if v.get() == 1:
        current_window = EnkrBesVDatoteko()
    elif v.get() == 2:
        current_window = DekrBesIzDatoteke()


if __name__ == '__main__':

    root = Tk()

    root.title("RSA kriptiranje")
    root.geometry('700x700')

    v = IntVar()
    #v = StringVar(root, "1")

    style = Style(root)
    style.configure("TRadiobutton",
                    foreground="black", font=("arial", 15, "bold"))
    # Dictionary to create multiple buttons
    values = {"Enkriptiraj datoteko v datoteko": 1,
              "Dekriptiraj besedilo iz datoteke": 2,
              "Poljubno dektriptiranje": 3,
              "Dekriptiranje poljubne datoteke": 4}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(root, text=text, variable=v,
                    value=value, command=windowChoice).pack(side=TOP, ipady=10)

    # Radiobutton1 = Radiobutton(
    #    root, text="1.moznost", variable=v, value=1, command=test).pack()
    # Radiobutton2 = Radiobutton(
    #    root, text="2.moznost", variable=v, value=2, command=test).pack()

    root.mainloop()

    # while True:
    #    choice = 0
    #    print("Izberite moznost:\n")
    #    print("1-Kriptiranje -> encrypted.txt\n")
    #    print("2-encrypted.txt -> Dekriptiranje\n")
    #    print("3-Poljubno dekriptiranje\n")
    #    print("4-Kriptiranje poljubne .txt datoteke -> encrypted.txt - in development\n")
    #    choice = int(input("Moznost: "))
#
    #    if choice == 1:
#
    #        print("Računanje vrednosti...")
#
    #        AllPrimesInRange()
    #        Define_p_q()
    #        CalculateTot()
    #        DefinePublic()
    #        DefinePrivate()
#
    #        message = input("\nVnesite sporočilo: \n")
    #        break
    #    elif choice == 2:
    #        print("\nVnesite zasebni ključ: ")
    #        n = int(input("n: "))
    #        d = int(input("d: "))
#
    #        print("\nOdpiranje .txt datoteke... \n")
    #        f = open("encrypted.txt", "r")
    #        cipher = f.read().split()
#
    #        f.close()
    #        break
    #    elif choice == 3:
    #        print("\nVnesite zasebni ključ: ")
    #        n = int(input("n: "))
    #        d = int(input("d: "))
#
    #        cipher = input("\nVnesite enrkiptirano sporočilo: ").split()
    #        break
    #    elif choice == 4:
    #        print("Računanje vrednosti...")
#
    #        AllPrimesInRange()
    #        Define_p_q()
    #        CalculateTot()
    #        DefinePublic()
    #        DefinePrivate()
#
    #        print("\nOdpiranje datoteke...")
#
    #        f = open("message.txt", "r")
    #        message = f.read()
#
    #        f.close()
    #        break
    #    else:
    #        print("----------------Nepravilno!------------")
#
    # if choice == 1 or choice == 4:
#
    #    for i in message:
    #        cipher.append((ord(i) ** e) % n)
#
    #    # writing to file
    #    f = open("encrypted.txt", "w")
    #    f.write(str(cipher))
    #    f.close()
#
    #    subprocess.run(["messageFormat.sh"], shell=True)
    #    print("\nEnkripcija končana, glej datoteko \"encrypted.txt\"\n")
    #    print("\nPritisni tipko ENTER za izhod...")
    #    input()
#
    # elif choice == 2 or choice == 3:
#
    #    for i in cipher:
    #        message.append((int(i) ** d) % n)
#
    #    print("\nDekodirano sporočilo: ")
    #    for i in message:
    #        print(chr(i), end='')
    #    print("\nPritisni tipko ENTER za izhod...")
    #    input()
