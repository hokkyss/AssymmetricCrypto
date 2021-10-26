def convert_to_asciis(string: str) -> str:
    result = ""
    for c in string:
        result = result.__add__(str(int(c)))
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
    temp: int = pow(x, y // 2) % p
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
    
    while u < 0:
        u += m
    return u
