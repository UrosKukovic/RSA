import random
import sys

in_message = []
out_message = []
choice = 0
key = (5*3)

primes = []
p = 0
q = 0
t = 0


def primes_in_range():
    min = 15000
    max = 25000

    for i in range(min, max):
        for x in range(2, i):
            if (i % x == 0):
                break
        else:
            primes.append(i)


def two_random_primes():

    while True:
        x = random.randint(0, (len(primes))-1)
        y = random.randint(0, (len(primes))-1)
        p = primes[x]
        q = primes[y]
        if p != q:
            break

    print(p, q)
    print(p*q)


#print("Izberite moznost:\n")
# print("1-Kriptiranje\n")
# print("2-Dekriptiranje\n")
#choice = int(input())
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
primes_in_range()

two_random_primes()
