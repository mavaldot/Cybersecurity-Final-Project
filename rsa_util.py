import math
from Crypto.Util import number

# print(number.getPrime(256))
# print(number.getPrime(128))

def generate_rsa(p_size, q_size):
    p = number.getPrime(p_size)
    q = number.getPrime(q_size)
    n = p*q
    lmbda = math.lcm(p - 1, q - 1)
    e = number.getPrime(max(p_size, q_size))
    d = pow(e, -1, lmbda)

    with open('priv_key.KEY', 'w') as f:
        f.write(f"{d};{n}")
    
    with open('pub_key.KEY', 'w') as f:
        f.write(f"{e};{n}")

generate_rsa(1024, 256)