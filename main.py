#-------------------------------------IMPORTS-------------------------------------#
import random
import sys
import os
import subprocess

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import pyperclip

#-------------------------------------VARIABLES-------------------------------------#
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


#-------------------------------------FUNCTIONS-------------------------------------#
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


def copy_to_clipboard(label_text):
    pyperclip.copy(label_text)


current_window = None


def OnSubmitEncryptText():
    global encrypt_window, n, d, e
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

    Label(encrypt_window, text="Message encrypted with key:", font=("Arial", 10, "bold")).grid(
        row=3, column=0)
    Label(encrypt_window, text="n:").grid(row=4, column=0, padx=10, pady=10)
    Label(encrypt_window, text="e:").grid(row=5, column=0, padx=10, pady=10)

    n_label = Label(encrypt_window, text=n, font=("Arial", 10, "bold"),
                    foreground="#655DBB", cursor='xterm')
    n_label.grid(row=4, column=1, padx=10, pady=10)

    e_label = Label(encrypt_window, text=e, font=("Arial", 10, "bold"),
                    foreground="#655DBB", cursor='xterm')
    e_label.grid(row=5, column=1, padx=10, pady=10)
    Button(encrypt_window, text="Copy", command=lambda: copy_to_clipboard(e)).grid(
        row=5, column=2)

    Label(encrypt_window, text="Use this to decrypt:", font=("Arial", 10, "bold")).grid(
        row=6, column=0)
    Label(encrypt_window, text="n:").grid(row=7, column=0, padx=10, pady=10)
    Label(encrypt_window, text="d:").grid(row=8, column=0, padx=10, pady=10)

    n_label = Label(encrypt_window, text=n, font=("Arial", 10, "bold"),
                    foreground="#655DBB", cursor='xterm')
    n_label.grid(row=7, column=1, padx=10, pady=10)
    Button(encrypt_window, text="Copy", command=lambda: copy_to_clipboard(n)).grid(
        row=7, column=2)

    d_label = Label(encrypt_window, text=d, font=("Arial", 10, "bold"),
                    foreground="#655DBB", cursor='xterm')
    d_label.grid(row=8, column=1, padx=10, pady=10)
    Button(encrypt_window, text="Copy", command=lambda: copy_to_clipboard(d)).grid(
        row=8, column=2)

    n_label.config(cursor='xterm')
    e_label.config(cursor='xterm')
    d_label.config(cursor='xterm')


def OnSubmitDecryptText():
    global dec_message_gui
    global decrypt_window
    global message, cipher, n, d

    dec_message_arr = []
    dec_message_gui = ""
    message = []

    n = int(n_gui.get("1.0", "end-1c"))
    d = int(d_gui.get("1.0", "end-1c"))

    print("\nOpening .txt file... \n")
    f = open("encrypted.txt", "r")
    cipher = f.read().split()
    f.close()

    for i in cipher:
        message.append((int(i) ** d) % n)

    for i in message:
        dec_message_arr.append(chr(i))

    dec_message_gui = ''.join(dec_message_arr)

    Label(decrypt_window, text="Decrypted message:", font=('Arial', 10)).grid(
        row=4, column=1, padx=5, pady=5)

    Label(decrypt_window, text=dec_message_gui, font=('Arial', 15, "bold"), foreground="#655DBB").grid(
        row=5, column=1, padx=5, pady=5)


def EncryptTextWindow():
    global Text_box
    global encrypt_window

    encrypt_window = tk.Tk()

    encrypt_window.title("Encrypt Text")
    # encrypt_window.geometry('400x400')

    Label(encrypt_window, text="Enter the message to encrypt:").grid(
        row=0, column=0)

    # create an input box and add it to the encrypt_window
    Text_box = tk.Text(encrypt_window, width=50, height=5,
                       font=('Arial, 12'))

    Text_box.grid(row=1, column=0)

    # create a button to submit the input
    submit_button = tk.Button(encrypt_window, text="Submit",
                              command=OnSubmitEncryptText)

    submit_button.grid(row=2, column=0)

    # Set the protocol to handle window closing
    encrypt_window.protocol("WM_DELETE_WINDOW", lambda: close_window(encrypt_window))

    return encrypt_window


def DecryptTextWindow():

    global n_gui
    global d_gui
    global decrypt_window
    decrypt_window = tk.Tk()

    decrypt_window.title("Decrypt Text")
    # decrypt_window.geometry('400x400')
    # create an input box and add it to the encrypt_window

    Label(decrypt_window, text="Enter the private key").grid(
        row=0, column=0, padx=10, pady=10)

    n_value = Label(decrypt_window, text="n = ")
    n_value.grid(row=1, column=0, pady=(0, 5), padx=5)

    d_value = Label(decrypt_window, text="d = ")
    d_value.grid(row=2, column=0, pady=(0, 15), padx=5)

    n_gui = tk.Text(decrypt_window, font=('Arial, 10'), width=15, height=1)
    n_gui.grid(row=1, column=1, pady=(0, 5), padx=5)

    d_gui = tk.Text(decrypt_window, font=('Arial, 10'), width=15, height=1)
    d_gui.grid(row=2, column=1, pady=(0, 15), padx=5)

    # create a button to submit the input
    submit_button = tk.Button(decrypt_window, text="Confirm",
                              command=OnSubmitDecryptText)
    submit_button.grid(row=1, column=2, padx=10, pady=10)

    # Set the protocol to handle window closing
    decrypt_window.protocol("WM_DELETE_WINDOW", lambda: close_window(decrypt_window))

    return decrypt_window


def CustomDecryptionWindow():
    window = Tk()

    # Set the protocol to handle window closing
    window.protocol("WM_DELETE_WINDOW",
                     lambda: close_window(window))

    window.title("Custom Decryption")
    window.geometry('400x400')

    # NOTE: not yet implemented - see README "Known limitations"
    Label(window, text="Custom decryption").pack()

    return window


def DecryptArbitraryFileWindow():
    window = Tk()

    # Set the protocol to handle window closing
    window.protocol(
        "WM_DELETE_WINDOW", lambda: close_window(window))

    window.title("Decrypt Arbitrary File")
    window.geometry('400x400')

    # NOTE: not yet implemented - see README "Known limitations"
    Label(window, text="Decrypt arbitrary file").pack()

    return window


def windowChoice():
    global current_window
    if current_window:
        current_window.destroy()
    if v.get() == 1:
        current_window = EncryptTextWindow()
    elif v.get() == 2:
        current_window = DecryptTextWindow()
    elif v.get() == 3:
        current_window = CustomDecryptionWindow()
    elif v.get() == 4:
        current_window = DecryptArbitraryFileWindow()


def close_window(window):
    global current_window
    current_window = None
    window.destroy()


if __name__ == '__main__':

    root = Tk()

    root.title("RSA Encryption")
    root.geometry('700x700')

    v = IntVar()

    style = Style(root)
    style.configure("TRadiobutton",
                    foreground="black", font=("arial", 15, "bold"))

    # Dictionary to create multiple buttons
    values = {"Encrypt text to file": 1,
              "Decrypt text from file": 2,
              "Custom decryption": 3,
              "Decrypt arbitrary file": 4}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(root, text=text, variable=v,
                    value=value, command=windowChoice).pack(side=TOP, ipady=10)

    root.mainloop()
