import random

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 33, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

EXPANSION = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]



def getRandom_N(r):
    number = ""
    for i in range(r):
        number += str(random.randint(0, 1))
    return number


def roundShift(bits, round):
    pass


def setBits(bits, table):
    n = len(table)
    newbits = ""
    for i in range(n):
        newbits += bits[table[i] - 1]
    return newbits


def expansion(bits):
    if (len(bits) != 32):
        raise Exception('Not the right length (32)')
    return setBits(bits, EXPANSION)


def initial_permutation(bits):
    if (len(bits) != len(IP)):
        raise Exception('Cant make the permutatioion IP because they are different lengths.')
    if (len(bits) != 64):
        raise Exception('Not the right length (64).')
    return setBits(bits, IP)


def xor(bits, key):
    if (len(bits) != len(key)):
        raise Exception("Can`t shift if they are different lengths")
    a=int(bits,2) ^ int(key,2)
    return str(bin(a))

def s_boxes(bits):


if __name__ == "__main__":
    generated = '1001111111011101110100011001010000111101100100110000010111001101'
    #print(len(expansion(generated[:32])))
    key='1000110101011101111010101000000110101111010111010001011000000111'
    #print(int(xor('10101','10101'),2))


