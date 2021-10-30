from .RSA import *
from .ElGamal import *
from .Paillier import *
# from .EllipticCurve import *
from .utils import *

def clean(text: str) -> List[int]:
    clean_text = text.replace(" ", "")
    int_arr = list(map(int, clean_text.split(",")))
    return int_arr

def proceed(public_key, private_key, choice, mode, message):
    if (mode == "Encryption"):
        if (choice == "RSA"):
            public_key_arr = clean(public_key)
            e, n = public_key_arr[0], public_key_arr[1]
            return rsa_encryption(message, n, e)
        
        if (choice == "Paillier"):
            public_key_arr = clean(public_key)
            g, n = public_key_arr[0], public_key_arr[1]
            return paillier_encryption(int(message), g, n)

    if (mode == "Decryption"):
        if (choice == "RSA"):
            private_key_arr = clean(private_key)
            d, n = private_key_arr[0], private_key[1]
            return rsa_decryption(message, n, d)
        
        if (choice == "Paillier"):
            private_key_arr = clean(private_key)
            lamda, miu, n = private_key_arr[0], private_key[1], private_key[2]
            return paillier_decryption(int(message), lamda, miu, n)

        

