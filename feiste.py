from utils import *
import hashlib
from perm_list import *


def get_innit_key(message):
    return hashlib.md5(message.encode('utf-8')).hexdigest()

def gen_keys(key):
    global p_list
    prev = get_innit_key(key)
    for p in p_list:
        curr = apply_permutation(p, prev)
        curr = hashlib.md5(curr.encode('utf-8')).hexdigest()
        prev = curr
        L, R = split128bits_in_half("{0:08b}".format(int(curr, 16)).ljust(128, '0'))
        yield XOR(L, R)

def use_s_box(bits64):
    global s_box
    retv = str()
    bits4_list = split_in_fours(bits64)
    for i, num in enumerate(bits4_list):
        retv += s_box[i][int(num, base=2)]
    return retv

def functionF(bits64, round_key):
    global p_feistel
    retv = use_s_box(bits64)
    retv = apply_permutation(p_feistel, retv)
    return retv

def util(message, ini_key, rev):
    roundkeys = list(gen_keys(ini_key))
    if rev:
        roundkeys.reverse()
    L, R = split128bits_in_half(message)
    for k in roundkeys:
        newL = R
        newR = XOR(L,functionF(R, k))
        L = newL
        R = newR
    return R+L

def feistel_encrypt(message,key):
    return util(message,key, False)
   
def feistel_decrypt(cipher,key):
    return util(cipher,key, True)

if __name__ == '__main__':
    key = 'secret key'
    message = intoBinStr("confidential message")[:128]
    cipher = feistel_encrypt(message, key)
    decrypted = feistel_decrypt(cipher, key)
    print("Plaintext (128 bits):\t", message)
    print("Ciphertext:\t\t", cipher)
    print("Decrypted message:\t", decrypted)
    print("XOR to compare\t\t", XOR(message, decrypted))