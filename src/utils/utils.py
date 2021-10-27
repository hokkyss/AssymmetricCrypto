from typing import ClassVar, Dict
from typing_extensions import Final

class StringEncoder:
    __CHAR_MAP: Final[ClassVar[Dict[str, str]]] = {
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
            result = result.__add__(StringEncoder.__CHAR_MAP[c])
        return result

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
