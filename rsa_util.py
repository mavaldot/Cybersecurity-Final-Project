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

    print(d)
    print(e)

generate_rsa(1024, 2048)