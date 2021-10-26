# ElGamal Algorithm

from textwrap import wrap
from typing import List, Tuple
from random import randint

from utils import inverse_modulo, pow_mod

def encrypt(m: List[int], public_key: Tuple[int, int, int]) -> List[Tuple[int, int]]:
    (p, g, y) = public_key

    k = randint(0, p - 1)

    result: List[Tuple[int, int]] = []
    for block in m:
        a = (g ** k) % p
        b = ((y ** k) * block) % p
        result.append((a, b))
    return result

def decrypt(m: List[Tuple[int, int]], private_key: Tuple[int, int]) -> List[int]:
    (p, x) = private_key

    result: List[int] = []

    for (a, b) in m:
        a = a % p; b = b % p

        inverse = inverse_modulo(pow_mod(a, x, p), p)
        result.append((b * inverse) % p)
    return result

def message_blocking(private: int, message: str, p: int) -> List[int]:
    digits: int = len(str(private))
    messages: List[int]
    try:
        messages = list(map(int, wrap(message, digits)))
        for block in messages:
            if (block >= p) or (block < 0):
                raise ValueError
    except:
        messages = list(map(int, wrap(message, digits - 1)))
    return messages

if __name__ == "__main__":
    print("p is public")
    p = int(input("p = any prime number = "))

    print("x is private. 1 <= x <=", p - 2)
    x = int(input("x = "))

    print("g is public. g <", p)
    g = int(input("g = "))

    print("y is public. y =", (g ** x) % p)
    y = (g ** x) % p

    print("public key: (p, g, y) =", (p, g, y))
    # private key = x

    m = input("message to be encrypted = ")
    m = message_blocking(x, m, p)

    encrypted = encrypt(m, public_key=(p, g, y))
    print(encrypted)

    decrypted = decrypt(encrypted, (p, x))
    print(decrypted)