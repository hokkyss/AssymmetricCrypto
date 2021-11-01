# Paillier Algorithm

from textwrap import wrap
from typing import List

from .utils import PG, lcm, inverse_modulo, pow_mod

def L(x, n):
    return (x - 1) / n

def get_miu(g: int, lamda: int, n: int):
    # x = (g ** lamda) % (n ** 2)
    x = pow_mod(g, lamda, n ** 2)
    return inverse_modulo(L(x, n), n)

# Encrypt the ciphertext with Paillier Algorithm
def paillier_encryption(m: int, g: int, n: int) -> int:
    # Nanti diganti sama generator
    r = 23
    # return ((g ** m) * (r ** n)) % (n ** 2)
    return pow_mod(g ** m, r ** n, n ** 2)

# Decrypt the ciphertext with Paillier Algorithm
def paillier_decryption(c: int, lamda: int, miu: int, n: int) -> int:
    x = (c ** lamda) % (n ** 2)
    # return (L(x, n) * miu) % n
    return pow_mod(L(x, n), miu, n)

# Generate paillier key
def generate_paillier_key():
    p = PG.random()
    q = PG.random()
    n = p * q
    lamda = lcm(p - 1, q - 1)
    g = n + 1
    miu = get_miu(g, lamda, n)
    public_key = [g, n]
    private_key = [lamda, miu, n]
    return [public_key, private_key]

# Main program to test
if (__name__ == "__main__"):
    PG = PrimeGenerator()
    p = PG.random()
    q = PG.random()
    n = p * q
    lamda = lcm(p - 1, q - 1)

    g = n+1
    print("Nilai p dan q\t\t:", p, ",", q)
    miu = get_miu(g, lamda, n)
    print("Public key\t\t:", g, ":", n)
    print("Private key\t\t:", lamda, ",", miu, ",", n)

    m = 42
    print("Message\t\t\t:", m)

    c = paillier_encryption(m, g, n)
    print("Cipherteks\t\t\t:", c)

    decrypted_m = paillier_decryption(c, lamda, miu, n)
    print("Decrypted\t\t\t:", decrypted_m)
