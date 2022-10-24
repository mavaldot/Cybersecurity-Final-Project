import hashlib
import sys
from rsa_util import read_private_key, read_public_key

BLOCKSIZE = 4096

def get_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(BLOCKSIZE), b""):
            sha256.update(block)

    return sha256.digest()

def create_signature(file, priv_key, password):
    hash = get_sha256(file)
    hash = int.from_bytes(hash, sys.byteorder)
    print('aaa')
    print(hash)
    d, n = read_private_key(priv_key, password)
    d, n = int(d), int(n)
    cipher = pow(hash, d, n)
    with open('signature.SIG', 'w') as f:
        f.write(str(cipher))  

def verify_signature(file, pub_key, signature):
    result = -1
    hash = get_sha256(file)
    hash = int.from_bytes(hash, sys.byteorder)
    e, n = read_public_key(pub_key)
    e, n = int(e), int(n)
    
    with open(signature, 'r') as f:
        cipher = int(f.readline())
        result = pow(cipher, e, n)

    return hash == result

create_signature('mateo.txt', 'priv_key.KEY', '1234')
a = verify_signature('mateo.txt', 'pub_key.KEY', 'signature.SIG')
print(a)

