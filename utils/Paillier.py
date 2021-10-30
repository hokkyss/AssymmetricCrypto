# Paillier Algorithm

from textwrap import wrap
from typing import List

from .utils import lcm, inverse_modulo, pow_mod

def L(x, n):
    return (x - 1) / n

def get_miu(g: int, lamda: int, n: int):
    x = (g ** lamda) % (n ** 2)
    return inverse_modulo(L(x, n), n)

# Encrypt the ciphertext with Paillier Algorithm
def paillier_encryption(m: int, g: int, n: int) -> int:
    # Nanti diganti sama generator
    r = 23
    return ((g ** m) * (r ** n)) % (n ** 2)
    # return pow_mod(g ** m, r ** n, n ** 2)

# Decrypt the ciphertext with Paillier Algorithm
def paillier_decryption(c: int, lamda: int, miu: int, n: int) -> int:
    x = (c ** lamda) % (n ** 2)
    return (L(x, n) * miu) % n
    # return pow_mod(L(x, n), miu, n)

# Main program to test
if (__name__ == "__main__"):
    p = int(input("Nilai p: "))
    q = int(input("Nilai q: "))
    n = p * q
    lamda = lcm(p - 1, q - 1)

    g = int(input("Nilai g: "))
    miu = get_miu(g, lamda, n)
    print(p, ":", q)
    print(g, ":", n)
    print(lamda, ":", miu)

    m = 42
    print(m)

    c = paillier_encryption(m, g, n)
    print(c)

    decrypted_m = paillier_decryption(c, lamda, miu, n)
    print(decrypted_m)
