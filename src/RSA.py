# RSA Algorithm

from textwrap import wrap
from typing import List

# Get the inverse modulo of e mod toi
def inverse_modulo(e: int, toi: int) -> int:
    k = 1
    val = (1 + (k * toi)) % e
    while (val != 0):
        k += 1
        val = (1 + (k * toi)) % e
    return int((1 + (k * toi)) / e)

# Get the greatest common divisor of a and b
def gcd(a: int, b: int) -> int:
    if (b == 0):
        return a
    if (a < b):
        return gcd(b, a)
    return gcd(b, a % b)

# Get the lowest common multiple
def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))

# Encrypt the ciphertext with RSA Algorithm
def rsa_encryption(m: List[int], n: int, e: int) -> List[int]:
    c = []
    for block in m:
        ci = (block ** e) % n
        c.append(ci)
    return c

# Decrypt the ciphertext with RSA Algorithm
def rsa_decryption(c: List[int], n: int, d: int) -> List[int]:
    m = []
    for block in c:
        mi = (block ** d) % n
        m.append(mi)
    return m

# Main program to test
if (__name__ == "__main__"):
    p = int(input("Nilai p: "))
    q = int(input("Nilai q: "))
    n = p * q
    toi = (p - 1) * (q - 1)

    e = int(input("Nilai e: "))
    d = inverse_modulo(e, toi)
    print(p, ":", q)
    print(n, ":", toi)
    print(e, ":", d)

    message = "07041111140011080204"
    m = wrap(message, 4)
    m = list(map(int, m))
    print(m)

    c = rsa_encryption(m, n, e)
    print(c)

    decrypted_m = rsa_decryption(c, n, d)
    print(decrypted_m)