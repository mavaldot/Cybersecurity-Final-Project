import tkinter as tk
import tkinter.simpledialog
from tkinter import ttk


import rsa_util as rutil
import rsa_signature as rsig

root = tk.Tk()
root.title("Signature Verifier")
root.geometry("480x480")

def create_signature_window():
    top = tk.Toplevel(root)
    top.geometry("480x480")
    top.title("Create signature")
    tk.Label(top, text="Wassup").pack()


def verify_signature_window():
    top = tk.Toplevel(root)
    top.geometry=("480x480")
    top.title("Verify a signature")
    tk.Label(top, text="FAFAFAFAF").pack()

def generate_keypair():
    print("hello man")
    user_pass = tk.simpledialog.askstring("Passowrd", "Please enter the password", show='*')
    rutil.generate_rsa(1024, 256, "1234")

rsa_button = ttk.Button(
    root,
    text="Generate RSA Key Pair",
    command=generate_keypair
)

create_signature_button = ttk.Button(
    root,
    text="Create a new signature",
    command=create_signature_window
)

verify_signature_button = ttk.Button(
    root,
    text="Check a signature",
    command=verify_signature_window
)

rsa_button.pack(padx=20, pady=20)
create_signature_button.pack(padx=20, pady=20)
verify_signature_button.pack(padx=20, pady=20)

root.mainloop()