import tkinter as tk
from tkinter import ttk

import cryptography as cr

root = tk.Tk()
root.title("Signature Verifier")
root.geometry("480x480")

def generate_keypair():
    print("hello man")

rsa_button = ttk.Button(
    root,
    text="Generate RSA Key Pair",
    command=generate_keypair
)

rsa_button.pack()

root.mainloop()