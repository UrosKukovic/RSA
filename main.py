import random
import sys
import os
import subprocess

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


if __name__ == '__main__':

    while True:
        choice = 0
        print("Izberite moznost:\n")
        print("1-Kriptiranje -> encrypted.txt\n")
        print("2-encrypted.txt -> Dekriptiranje\n")
        print("3-Poljubno dekriptiranje - ni še dodano!\n")
        choice = int(input("Moznost: "))

        if choice == 1:

            print("Računanje vrednosti...")

            AllPrimesInRange()
            Define_p_q()
            CalculateTot()
            DefinePublic()
            DefinePrivate()

            message = input("\nVnesite sporocilo: \n")
            break
        elif choice == 2:
            print("\nVnesite zasebni ključ: ")
            n = int(input("n: "))
            d = int(input("d: "))

            print("\nOdpiranje .txt datoteke... \n")
            f = open("encrypted.txt", "r")
            cipher = f.read().split()

            #cipher = input("Vnesite kriptirano sporočilo\n").split()
            f.close()
            break
        else:
            print("----------------Nepravilno!------------")

    if choice == 1:

        for i in message:
            cipher.append((ord(i) ** e) % n)

        # writing to file
        f = open("encrypted.txt", "w")
        f.write(str(cipher))
        f.close()

        subprocess.run(["messageFormat.sh"], shell=True)
        print("\nEnkripcija končana, glej datoteko \"encrypted.txt\"\n")
        print("\nPritisni tipko ENTER za izhod...")
        input()

    if choice == 2:

        for i in cipher:
            message.append((int(i) ** d) % n)

        print("\nDekodirano sporočilo: ")
        for i in message:
            print(chr(i), end='')
        print("\nPritisni tipko ENTER za izhod...")
        input()
