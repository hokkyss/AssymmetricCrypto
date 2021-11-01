# Paillier Algorithm

import random
from textwrap import wrap
from typing import List

from .utils import PG, lcm, gcd

# Get the L value based on x and n
def L(x, n):
    return int((x - 1) / n)

# Get the miu value based on g, lamda, and n value
def get_miu(g: int, lamda: int, n: int):
    x = pow(g, lamda, n ** 2)
    return pow(L(x, n), -1, n)

# Encrypt the ciphertext with Paillier Algorithm
def paillier_encryption(m: int, g: int, n: int) -> int:
    r = PG.random_below(n)
    return pow(pow(g, m, n * n) * pow(r, n, n * n), 1, n * n)

# Decrypt the ciphertext with Paillier Algorithm
def paillier_decryption(c: int, lamda: int, miu: int, n: int) -> int:
    x = pow(c, lamda, n ** 2)
    return pow(L(x, n) * miu, 1, n)

# Generate paillier key
def generate_paillier_key():
    p = PG.random()
    q = PG.random()
    n = p * q
    toi = (p - 1) * (q - 1)
    while (gcd(n, toi) != 1):
        p = PG.random()
        q = PG.random()
        n = p * q
        toi = (p - 1) * (q - 1)

    lamda = lcm(p - 1, q - 1)
    g = n + 1
    miu = get_miu(g, lamda, n)
    public_key = [g, n]
    private_key = [lamda, miu, n]
    return [public_key, private_key]

# Main program to test
if (__name__ == "__main__"):
    all_key = generate_paillier_key()
    g = all_key[0][0]
    n = all_key[0][1]
    lamda = all_key[1][0]
    miu = all_key[1][0]
    miu = get_miu(g, lamda, n)
    print("Public key\t\t:", g, ":", n)
    print("Private key\t\t:", lamda, ",", miu, ",", n)

    m = random.randint(0, n)
    print("Message\t\t\t:", m)

    c = paillier_encryption(m, g, n)
    print("Cipherteks\t\t:", c)

    decrypted_m = paillier_decryption(c, lamda, miu, n)
    print("Decrypted\t\t:", decrypted_m)