import hashlib
import sys
from rsa_util import read_private_key, read_public_key

BLOCKSIZE = 4096
SIGNATURE_FOLDER = "signatures/"

"""
This module deals with creating and verifying the signature
"""

def get_sha256(filepath):
    """
    This module gets the sha256 hash of the file indicated by the filepath
    It can read large files by reading blocks of 4096 bytes iteratively
    """
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(BLOCKSIZE), b""):
            sha256.update(block)

    return sha256.digest()

def create_signature(file, priv_key, password):
    """
    This function creates the signautre given a file, a private key, and a password
    A hash from the file is obtained, then uses the private key to create a cipher
    The signature is created with a .SIG extension
    """
    hash = get_sha256(file)
    hash = int.from_bytes(hash, sys.byteorder)
    d, n = read_private_key(priv_key, password)
    d, n = int(d), int(n)
    cipher = pow(hash, d, n)

    signature_name = file.split('/').pop()

    with open(SIGNATURE_FOLDER+f'{signature_name}.SIG', 'w') as f:
        f.write(str(cipher))  

def verify_signature(file, pub_key, signature):
    """
    This function verifies a signature given the file, the public key and the signature file.
    A hash from the file is compared with the signature decrypted with the public key
    If the signature is valid, returns true. Otherwise, return false.
    """
    result = -1
    hash = get_sha256(file)
    hash = int.from_bytes(hash, sys.byteorder)
    e, n = read_public_key(pub_key)
    e, n = int(e), int(n)
    
    with open(signature, 'r') as f:
        cipher = int(f.readline())
        result = pow(cipher, e, n)

    return hash == result