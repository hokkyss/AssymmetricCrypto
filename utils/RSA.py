# RSA Algorithm

from textwrap import wrap
from typing import List

from utils import pow_mod, inverse_modulo

def text_to_block(text: str, block_size: int) -> List[int]:
    blocks = wrap(text, block_size)
    blocks = list(map(int, blocks))
    return blocks

def block_to_text(m: List[int], block_size: int) -> str:
    final_m = []
    print_format = "0" + str(block_size) + "d"
    for block in m:
        final_m.append(format(block, print_format))
    return "".join(final_m)

# Encrypt the ciphertext with RSA Algorithm
def rsa_encryption(message: str, n: int, e: int, block_size: int = 4) -> str:
    m = text_to_block(message, block_size)
    c = []
    for block in m:
        ci = pow_mod(block, e, n)
        c.append(ci)
    return block_to_text(c, block_size)

# Decrypt the ciphertext with RSA Algorithm
def rsa_decryption(ciphertext: str, n: int, d: int, block_size: int = 4) -> str:
    c = text_to_block(ciphertext, block_size)
    m = []
    for block in c:
        mi = pow_mod(block, d, n)
        m.append(mi)
    return block_to_text(m, block_size)

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
    print(message)

    ciphertext = rsa_encryption(message, n, e)
    print(ciphertext)

    decrypted_m = rsa_decryption(ciphertext, n, d)
    print(decrypted_m)