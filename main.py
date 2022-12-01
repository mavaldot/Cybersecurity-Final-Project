import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import rsa_util as rutil
import rsa_signature as rsig

"""
This is the main module of the cibersecurity-final-project.
"""

KEYS_FOLDER = 'keys'
SIGNATURES_FOLDER = 'signatures'

def generate_keypair():
    """
    Command for the generate_rsa_button (Generate a private and public key).

    Ask the user for a password and an optional key name in order to generate the private and public keys with RSA.
    """

    user_pass = tk.simpledialog.askstring("Password", "Please enter the password", show='*')
    
    if (user_pass== None) or (not user_pass.strip()):
        tkinter.messagebox.showerror(title="Error", message="Please make sure you write the password.")
        return

    key_name = tk.simpledialog.askstring("Key Name", "Please enter the key name \n(leave blank if you want to save the keys in the root folder) ")
    if key_name== None:
        key_name = ""

    rutil.generate_rsa(1024, 256, user_pass, key_name)
    tkinter.messagebox.showinfo(title=None, message="KEYPAIR generated successfully!")

def create_signature():
    """
    Command for the create_signature_button (Create the signature of a document).

    First, the user specifies the file he wants to sign. Then, the user chooses a private key and types the password. Finally, it creates the document's signature.
    """
    tkinter.messagebox.showinfo(title=None, message="Please choose the FILE you want to SIGN")
    filepath = askopenfilename(title="Please pick the FILE")
    if not filepath.strip():
        tkinter.messagebox.showerror(title="Error", message="Please make sure you chose a file.")
        return

    tkinter.messagebox.showinfo(title=None, message="Please choose the PRIVATE KEY")
    private_key = askopenfilename(title="Please pick the PRIVATE KEY", initialdir = KEYS_FOLDER)
    if not private_key.strip():
        tkinter.messagebox.showerror(title="Error", message="Please make sure you chose a file.")
        return

    tkinter.messagebox.showinfo(title=None, message="Please enter the PASSWORD for the PRIVATE KEY")
    user_pass = tk.simpledialog.askstring("Password", "Please enter the private key's password", show='*')

    try:
        rsig.create_signature(filepath, private_key, user_pass)
        tkinter.messagebox.showinfo(title=None, message="Signature created successfully!")
    except Exception as e:
        tkinter.messagebox.showerror(title="Exception", message=f"Please make sure you chose the correct file and entered the correct password. {e}")

def verify_signature():
    """
    Command for the verify_signature_button (Verify the signature of a document).

    First, the user specifies the original file and its signature. Then, the user chooses the public key used to sign the document. Finally, it verifies the signature.
    """
    tkinter.messagebox.showinfo(title=None, message="Please choose the FILE you want to VERIFY")
    filepath = askopenfilename(title="Please pick the FILE")
    if not filepath.strip():
        tkinter.messagebox.showerror(title="Error", message="Please make sure you chose a file.")
        return

    tkinter.messagebox.showinfo(title=None, message="Please choose the SIGNATURE you want to verify")
    signature = askopenfilename(title="Please pick the SIGNATURE", initialdir = SIGNATURES_FOLDER)
    if not signature.strip():
        tkinter.messagebox.showerror(title="Error", message="Please make sure you chose a file.")
        return
    
    tkinter.messagebox.showinfo(title=None, message="Please choose the PUBLIC KEY")
    public_key = askopenfilename(title="Please pick the PUBLIC KEY", initialdir = KEYS_FOLDER)
    if not public_key.strip():
        tkinter.messagebox.showerror(title="Error", message="Please make sure you chose a file.")
        return

    try:
        verification = rsig.verify_signature(filepath, public_key, signature)
        if (verification):
            tkinter.messagebox.showinfo(title=None, message="The signature is CORRECT!")
        else:
            tkinter.messagebox.showwarning(title=None, message="The signature does NOT match the file and key!")
    except Exception as e:
        tkinter.messagebox.showerror(title="Exception", message=f"{e}")

# Tkinter (GUI)
root = tk.Tk()
root.title("Signature Verifier")
root.geometry("480x480")

generate_rsa_button = ttk.Button(
    root,
    text="Generate RSA Key Pair",
    command=generate_keypair
)
generate_rsa_button.pack(padx=20, pady=20)

create_signature_button = ttk.Button(
    root,
    text="Create a new signature",
    command=create_signature
)
create_signature_button.pack(padx=20, pady=20)

verify_signature_button = ttk.Button(
    root,
    text="Check a signature",
    command=verify_signature
)
verify_signature_button.pack(padx=20, pady=20)

root.mainloop()