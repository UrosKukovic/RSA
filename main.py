in_message = []
out_message = []
choice = 0
key = (5*3)


print("Izberite moznost:\n")
print("1-Kriptiranje\n")
print("2-Dekriptiranje\n")
choice = int(input())
if choice == 1:
    print("\nVnesite sporocilo: \n")
    in_message = input()

elif choice == 2:
    print("\nVnesite sporocilo: \n")
    in_message = input().split()

else:
    print("Nepravilno!")

if choice == 1:
    for i in in_message:
        out_message.append(ord(i))

    for x in out_message:
        print(x*key)

elif choice == 2:
    for i in in_message:
        rez = int(i)/key
        out_message.append(rez)

    for i in out_message:
        print(chr(int(i)))
