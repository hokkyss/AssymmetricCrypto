from typing_extensions import Literal
from .RSA import *
from .ElGamal import *
from .Paillier import *
from .EllipticCurve import *
from .utils import *

# Read the file and return the content of the file
def readFile(filename: str) -> str:
    f = open("keys/" + filename, "r")
    output_text = f.read()
    return output_text

# Clean the key into list of value contain in key
def clean(text: str) -> List[int]:
    clean_text = text.replace(" ", "")
    int_arr = list(map(int, clean_text.split(",")))
    return int_arr

# Generate the key based on user choice
def generateKey(choice):
    print(choice)
    all_keys = None
    filename = ""
    id = random.randint(0, 1000)
    if (choice == "RSA"):
        all_keys = generate_rsa_key()
        filename = "rsa-" + str(id)

    elif (choice == "ElGamal"):
        # TO DO LIST HOKKI
        all_keys = [[],[]]
        filename = "elgamal-" + str(id)

    elif (choice == "Paillier"):
        all_keys = generate_paillier_key()
        filename = "paillier-" + str(id)

    elif (choice == "ECC"):
        # TO DO LIST HOKKI
        all_keys = [[],[]]
        filename = "ecc-" + str(id)

    public_key = ','.join(list(map(str, all_keys[0])))
    private_key = ','.join(list(map(str, all_keys[1])))
    full_path = "keys/" + filename
    
    f = open(full_path + ".pub", 'w')
    f.write(public_key)
    f.close()

    f = open(full_path + ".pri", 'w')
    f.write(private_key)
    f.close()

    notification = "\nGenerate key success! Saved on " + full_path
    notification += "\nPublic key : " + public_key
    notification += "\nPrivate key : " + private_key
    return notification


def proceed(public_key, private_key, choice: Literal['RSA', 'ElGamal', 'Paillier', 'Elliptic Curve Cryptography'], mode: Literal['Encryption', 'Decryption'], message: str):
    if not choice:
        raise ValueError('You must choose a Cryptography Algorithm.')
    if not mode:
        raise ValueError('You must either encrypt or decrypt')

    if (mode == "Encryption"):
        if (choice == "RSA"):
            try:
                public_key_arr = clean(public_key)
                e, n = public_key_arr[0], public_key_arr[1]
                return rsa_encryption(message, n, e)
            except:
                raise ValueError('Public key format: <e>, <n>')
        if (choice == "Paillier"):
            try:
                public_key_arr = clean(public_key)
                g, n = public_key_arr[0], public_key_arr[1]
                return paillier_encryption(int(message), g, n)
            except:
                raise ValueError('Public key format: <g>, <n>')
        if (choice == "ElGamal"):
            try:
                public_key_arr = clean(public_key)
                [p, g, y] = public_key_arr

                message_block = message_blocking(p, message, p)
                return ElGamal.encrypt(message_block, (p, g, y))
            except:
                raise ValueError('Public key format: <p>, <g>, <y>')
        if (choice == "Elliptic Curve Cryptography"):
            try:
                public_key_arr = clean(public_key)

                [Bx, By, PbX, PbY] = public_key_arr

                B = EllipticCurve(Bx, By)
                mess = EllipticCurve.encode(message)

                return B.encrypt(mess, (PbX, PbY))
            except:
                raise ValueError('Public key format: <B.x>, <B.y>, <Pb.x>, <Pb.y>')
    if (mode == "Decryption"):
        if (choice == "RSA"):
            try:
                private_key_arr = clean(private_key)
                d, n = private_key_arr[0], private_key_arr[1]
                return rsa_decryption(message, n, d)
            except:
                raise ValueError('Private key format: <d>, <n>')    
        if (choice == "Paillier"):
            try:
                private_key_arr = clean(private_key)
                lamda, miu, n = private_key_arr[0], private_key_arr[1], private_key_arr[2]
                return paillier_decryption(int(message), lamda, miu, n) 
            except:
                raise ValueError('Private key format: <λ>, <µ>, <n>')
        if (choice == "ElGamal"):
            try:
                public_key_arr = clean(public_key)
                [p, g, y] = public_key_arr

                message_block = message_blocking(p, message, p)
                return ElGamal.encrypt(message_block, (p, g, y))
            except:
                raise ValueError('Public key format: <p>, <g>, <y>')
        if (choice == "Elliptic Curve Cryptography"):
            try:
                public_key_arr = clean(public_key)

                [Bx, By, PbX, PbY] = public_key_arr
                return EllipticCurve.encrypt(message, (Bx, By), (PbX, PbY))
            except:
                raise ValueError('Public key format: <B.x>, <B.y>, <p>, <Pb.x>, <Pb.y>, <a>, <b>')
