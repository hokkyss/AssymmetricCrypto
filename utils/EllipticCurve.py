from typing import ClassVar, List, Tuple
from typing_extensions import Final, final

from .utils import inverse_modulo, pow_mod

@final
class EllipticCurve:
    __INFINITY: Final[ClassVar[Tuple[int, int]]] = (0, 10000000000000000000000000000000000000000000000000000000000000000)

    @staticmethod
    def multiply(P: Tuple[int, int], k: int, p: int) -> Tuple[int, int]:
        """
        Count multiplication using divide and conquer algorithm
        """
        if k < 0:
            (xR, yR) = EllipticCurve.multiply(P, -k, p)
            return (xR, -yR)
        if k == 0:
            return EllipticCurve.__INFINITY
        if k == 1:
            return P
        
        multiplier = k // 2
        remainder = k % 2

        temp = EllipticCurve.multiply(P, multiplier, p)
        return EllipticCurve.add(EllipticCurve.multiply(temp, 2, p), EllipticCurve.multiply(P, remainder, p), p)

    @staticmethod
    def add(P: Tuple[int, int], Q: Tuple[int, int], p: int) -> Tuple[int, int]:
        (xP, yP) = P
        (xQ, yQ) = Q
        (_, yO) = EllipticCurve.__INFINITY

        if yP == yO:
            return Q
        if yQ == yO:
            return P
        if (xP == xQ) and (yP == -yQ):
            return EllipticCurve.__INFINITY
        
        m = (((yP - yQ) % p) * inverse_modulo((xP - xQ), p)) % p

        xR = (pow_mod(m, 2, p) - xP - xQ) % p
        yR = ((m(xP - xR)) % p - yP) % p
        
        return (xR, yR)
    
    @staticmethod
    def generate(a: int, b: int, p: int) -> List[Tuple[int, int]]:
        """
        Generate all points (x, y) on Elliptic Curve satisfying
        y ** 2 = x ** 3 + ax + b
        """
        assert ((4 * pow_mod(a, 3, p)) + (27 * pow_mod(b, 2, p))) % p != 0

        results: List[Tuple[int, int]] = []

        modulo_table: List[int] = []
        for i in range(0, p, 1):
            modulo_table.append((pow_mod(i, 3, p) + ((a * i) % p) + b) % p)
        
        pass