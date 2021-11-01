import random
import numpy as np
from typing import ClassVar, Dict, List

class StringEncoder:
    __CHAR_MAP: ClassVar[Dict[str, str]] = {
        "0": "00",
        "1": "01",
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        "6": "06",
        "7": "07",
        "8": "08",
        "9": "09",
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
        "G": "16",
        "H": "17",
        "I": "18",
        "J": "19",
        "K": "20",
        "L": "21",
        "M": "22",
        "N": "23",
        "O": "24",
        "P": "25",
        "Q": "26",
        "R": "27",
        "S": "28",
        "T": "29",
        "U": "30",
        "V": "31",
        "W": "32",
        "X": "33",
        "Y": "34",
        "Z": "35"
    }

    @staticmethod
    def encode(string: str) -> str:
        result = ""
        for c in string:
            result = result + StringEncoder.__CHAR_MAP[c]
        return result

class PrimeGenerator:
    __PRIMES: List[int]

    def __init__(self) -> None:
        # Generate List of Prime Number
        self.__PRIMES = []
        n = 10000000
        prime = [True] * n
        for i in range(3, int(n**0.5)+1, 2):
            if prime[i]:
                prime[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)

        self.__PRIMES = [2] + [i for i in range(3,n,2) if prime[i]]
        print("SELESAI")

    def random(self):
        return random.choice(self.__PRIMES)
    
    def random_below(self, n):
        filtered_prime = [x for x in self.__PRIMES if x <= n]
        selected_prime = random.choice(filtered_prime)
        while (gcd(selected_prime, n) != 1):
            selected_prime = random.choice(filtered_prime)
        return selected_prime

def pow_mod(x: int, y: int, p: int) -> int:
    """
    Count (x ** y) % p using divide and conquer.

    x > 0
    """
    assert x > 0
    x = x % p

    if y == 0: return 1
    if y == 1: return x % p
    temp: int = pow_mod(x, y // 2, p)
    return (temp * temp * pow(x, y % 2)) % p

def gcd(a: int, b: int) -> int:
    if a == 0: return b
    return gcd(b % a, a)

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

def inverse_modulo(a: int, m: int) -> int:
    """
    Count (1 / a) % m using bezout identity.
    @documentation https://www.dcode.fr/bezout-identity
    """
    assert gcd(a, m) == 1

    r = a; r_ = m
    u = 1; u_ = 0
    v = 0; v_ = 1
    while r_ != 0:
        q = r // r_
        r_temp = r;             u_temp = u;             v_temp = v
        r = r_;                 u = u_;                 v = v_
        r_ = r_temp - (q * r_); u_ = u_temp - (q * u_); v_ = v_temp - (q * v_)
    
    # if u is negative, u becomes positive.
    return u % m

PG = PrimeGenerator()