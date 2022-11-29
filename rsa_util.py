import math
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Util import number

KEY_FOLDER = 'keys/'

def generate_rsa(p_size, q_size, password):
    p = number.getPrime(p_size)
    q = number.getPrime(q_size)
    n = p*q
    lmbda = math.lcm(p - 1, q - 1)
    e = number.getPrime(max(p_size, q_size))
    d = pow(e, -1, lmbda)

    password = bytes(password, "utf-8")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'0',
        iterations=1000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    with open(KEY_FOLDER+"priv_key.KEY", "wb") as f:
        secret_key = f"{d};{n}"
        f.write(fernet.encrypt(secret_key.encode('utf-8')))
    
    with open(KEY_FOLDER+"pub_key.KEY", "w") as f:
        f.write(f"{e};{n}")

def read_public_key(path):
    arr = []
    with open(path, "r") as f:
        data = f.readline()
        arr = data.split(";")
    
    if len(arr) != 2:
        raise Exception("Invalid key")

    return arr[0], arr[1]

def read_private_key(path, password):
    arr = []
    password = bytes(password, "utf-8")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'0',
        iterations=1000
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()
        decoded_data = fernet.decrypt(data).decode("utf-8")
        arr = decoded_data.split(";")

    if len(arr) != 2:
        raise Exception("Invalid key")

    return arr[0], arr[1]