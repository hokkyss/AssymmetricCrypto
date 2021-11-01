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
            d, n = private_key_arr[0], private_key_arr[1]
            return rsa_decryption(message, n, d)
        
        if (choice == "Paillier"):
            private_key_arr = clean(private_key)
            lamda, miu, n = private_key_arr[0], private_key_arr[1], private_key_arr[2]
            return paillier_decryption(int(message), lamda, miu, n)

        

