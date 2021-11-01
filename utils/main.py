from .RSA import *
from .ElGamal import *
from .Paillier import *
# from .EllipticCurve import *
from .utils import *

def generateKey(choice):
    print(choice)
    all_keys = None
    filename = ""
    id = random.randint(0, 1000)
    if (choice == "RSA"):
        all_keys = generate_rsa_key()
        filename = "rsa-" + str(id)

    elif (choice == "ElGamal"):
        all_keys = [[],[]]
        filename = "elgamal-" + str(id)

    elif (choice == "Paillier"):
        all_keys = generate_paillier_key()
        filename = "paillier-" + str(id)

    elif (choice == "ECC"):
        all_keys = [[],[]]
        filename = "ecc-" + str(id)

    public_key = list(map(str, all_keys[0]))
    private_key = list(map(str, all_keys[1]))
    path = "keys/"
    
    f = open(path + filename + ".pub", 'w')
    f.write(','.join(public_key))
    f.close()

    f = open(path + filename + ".pri", 'w')
    f.write(','.join(private_key))
    f.close()

    return all_keys, path + filename

def clean(text: str) -> List[int]:
    clean_text = text.replace(" ", "")
    int_arr = list(map(int, clean_text.split(",")))
    return int_arr

def proceed(public_key, private_key, choice, mode, message):
    print(choice)
    print(mode)
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
            d, n = private_key_arr[0], private_key_arr[1]
            return rsa_decryption(message, n, d)
        
        if (choice == "Paillier"):
            private_key_arr = clean(private_key)
            lamda, miu, n = private_key_arr[0], private_key_arr[1], private_key_arr[2]
            return paillier_decryption(int(message), lamda, miu, n)

        

