import random
import sys

in_message = []
out_message = []
choice = 0
key = (5*3)

primes = []
p = 0
q = 0

tot = 0

n = 0
e = 0
d = 0


FermatPrimes = [3, 5, 17, 257, 65537, 42944967297]


def PrimesInRange():
    min = 10
    max = 50

    for i in range(min, max):
        for x in range(2, i):
            if (i % x == 0):
                break
        else:
            primes.append(i)


def TwoRandomPrimes():
    global p, q
    while True:
        x = random.randint(0, (len(primes))-1)
        y = random.randint(0, (len(primes))-1)
        p = primes[x]
        q = primes[y]
        if p != q:
            break

    print("p: ", p, "q: ", q)


def defineRestOfRSA():
    global n, e
    n = p*q
    print("n:", n)

    x = random.randint(0, (len(FermatPrimes))-1)
    e = FermatPrimes[x]
    print("e: ", e)


def ComputeTot():

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


def modInverse(e, tot):

    for X in range(1, tot):
        if (((e % tot) * (X % tot)) % tot == 1):
            return X
    return -1

    # print("Izberite moznost:\n")
    # print("1-Kriptiranje\n")
    # print("2-Dekriptiranje\n")
    # choice = int(input())
    # if choice == 1:
    #    print("\nVnesite sporocilo: \n")
    #    in_message = input()
    #
    # elif choice == 2:
    #    print("\nVnesite sporocilo: \n")
    #    in_message = input().split()
    #
    # else:
    #    print("Nepravilno!")
    #
    # if choice == 1:
    #    for i in in_message:
    #        out_message.append(ord(i))
    #
    #    for x in out_message:
    #        print(x*key)
    #
    # elif choice == 2:
    #    for i in in_message:
    #        rez = int(i)/key
    #        out_message.append(rez)
    #
    #    for i in out_message:
    #        print(chr(int(i)))
    #


PrimesInRange()

TwoRandomPrimes()

defineRestOfRSA()

ComputeTot()
