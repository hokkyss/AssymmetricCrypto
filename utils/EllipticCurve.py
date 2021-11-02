from typing import ClassVar, Dict, List, Tuple
from random import randint

from .utils import StringEncoder, inverse_modulo, pow_mod

class EllipticCurve:
    __INFINITY: ClassVar[Tuple[int, int]] = (0, 10000000000000000000000000000000000000000000000000000000000000000)
    __k: ClassVar[int] = 2957
    __a: ClassVar[int] = 2969
    __b: ClassVar[int] = 2971
    __p: ClassVar[int] = 2999
    __table: ClassVar[List[int]] = []

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        p = EllipticCurve.__p

        if len(EllipticCurve.__table) == 0:
            for i in range(p):
                EllipticCurve.__table.append(pow_mod(i, 2, p))

    def multiply(self, k: int):
        if k < 0:
            negative = self.multiply(-k)
            return EllipticCurve(negative.x, -negative.y)
        if k == 0:
            (xO, yO) = EllipticCurve.__INFINITY
            return EllipticCurve(xO, yO)
        if k == 1:
            return self

        multiplier = k // 2
        remainder = k % 2

        temp = self.multiply(multiplier)

        return temp.add(temp).add(self.multiply(remainder))

    def add(self, other):
        (xP, yP) = self.x, self.y

        xQ: int; yQ: int
        (xQ, yQ) = other.x, other.y
        (xO, yO) = EllipticCurve.__INFINITY

        p = EllipticCurve.__p

        if yP == yO:
            return other
        if yQ == yO:
            return self
        if (xP == xQ) and (yP == -yQ):
            return EllipticCurve(xO, yO)
        if (xP == xQ) and (yP == yQ):
            m = inverse_modulo(2 * yP, p) * (3 * pow_mod(xP, 2, p) + EllipticCurve.__a) % p

            xR = (pow_mod(m, 2, p) - (2 * xP)) % p
            yR = (m * (xP - xR) - yP) % p
            return EllipticCurve(xR, yR)

        m = (((yP - yQ) % p) * inverse_modulo((xP - xQ) % p, p)) % p

        xR = (pow_mod(m, 2, p) - xP - xQ) % p
        yR = (((m * (xP - xR)) % p) - yP) % p

        return EllipticCurve(xR, yR)

    def subtract(self, other):
        return self.add(other.multiply(-1))

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    @staticmethod
    def encode(m: str) -> List[Tuple[int, int]]:
        result: List[Tuple[int, int]] = []
        table = EllipticCurve.__table
        k = EllipticCurve.__k
        taken: List[List[bool]] = [[False for _ in range(len(table))] for __ in range(len(table))]

        encoding_map: Dict[str, Tuple[int, int]] = {}
        for c in m:
            try:
                result.append(encoding_map[c])
            except:
                in_int = StringEncoder.encode(c)
                p = EllipticCurve.__p
                a = EllipticCurve.__a
                b = EllipticCurve.__b

                y: int = None
                for x in range(in_int * k + 1, in_int * k + 1 + p):
                    x = x % p
                    kuadrat = (pow_mod(x, 3, p) + x * a + b) % p
                    for i in range(p):
                        if taken[x][i]:
                            continue
                        if table[i] == kuadrat:
                            y = i
                            break
                    if y != None:
                        taken[x][y] = True
                        encoding_map[c] = (x, y)
                        break
                if not y:
                    (x, y) = EllipticCurve.__INFINITY
                result.append((x, y))
        
        print(result)
        return result

    @staticmethod
    def decode(P: Tuple[int, int]) -> str:
        return "A"

    def encrypt(self, m: List[Tuple[int, int]], public_key: Tuple[str, str]):
        """
        - `m` list of ECCPoints
        - `p` is any prime number
        - `public_key` is Pb
        - `param` is (a, b) of the used elliptic curve for encoding
        """
        result: List[Tuple[str, str]] = []
        (xpub, ypub) = public_key
        public = EllipticCurve(xpub, ypub)

        for Pm in m:
            (x, y) = Pm
            k = randint(1, EllipticCurve.__p - 1)

            Pc = (str(self.multiply(k)), str(EllipticCurve(x, y).add(public.multiply(k))))
            result.append(Pc)
        return result

    @staticmethod
    def decrypt(m: List[Tuple[Tuple[int, int], Tuple[int, int]]], private_key: int) -> List[int]:
        result: List[str] = []
        p = EllipticCurve.__p

        for (a, b) in m:
            (xa, ya) = a
            (xb, yb) = b

            if (xa < 0) or (xa >= p) or (ya < 0) or (ya >= p) or (xb < 0) or (xb >= p) or (yb < 0) or (yb >= p):
                raise ValueError(f'Each number must be between {0} and {p - 1}, inclusively!')

            subtractor = EllipticCurve(xa, ya).multiply(private_key)
            Pm = EllipticCurve(xb, yb).subtract(subtractor)

            result.append(str(Pm))
        print(result)
        return result
