def XOR(bits1,bits2):
    # ciągi muszą być równej długości
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]: 
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

def split128bits_in_half(binarybits):
    return binarybits[:64], binarybits[64:]

#Funkcje pomocnicze
get_bin = lambda x, n: format(x, 'b').zfill(n)

#tablica znaków w tablicę kodów int
def intoIntArray(message: str):
    int_array = []
    mesg_array = list(message) 
    for i in mesg_array:
        int_array.append(ord(i))
    return int_array

#tablica kodów int w tablice znaków 
def intoCharArray(message: list()):
    mesg_char = []
    for i in message:
        mesg_char.append(chr(i))
    return mesg_char

def intListToBinStr(message_list):
    binary = []
    for x in message_list: 
        binary.append(get_bin(x, 8))
    binary_str = ""
    for x in binary:
        binary_str+=x 
    return binary_str

def intoBinStr(message):
    return intListToBinStr(intoIntArray(message))

def  apply_permutation(P_TABLE, PLAINTEXT):
    permutated_M = ""
    for index in P_TABLE:
        permutated_M += PLAINTEXT[int(index)]
    return permutated_M

def split_in_fours(bits64):
    return [bits64[i:i+4] for i in range(0, len(bits64), 4)]


if __name__ == '__main__':
    M = "Attack!!"
    key = "EagleHasLanded" 

    plaintext = intoBinStr(M) 
    print("Plaintext (64 bits):", plaintext)
    binary_key = intoBinStr(key) 
    print("Key (only 64 bits): ", binary_key[:64])
