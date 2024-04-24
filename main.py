import random


class Constants:
    def __init__(self):
        self.GENERATED = '1001111111011101110100011001010000111101100100110000010111001101'
        self.KEY = '1000110101011101111010101000000110101111010111010001011000000111'
        self.EMPTY = '0000000000000000000000000000000000000000000000000000000000000000'

    @property
    def KEY2(self):
        return self.KEY

    @property
    def GENERATED2(self):
        return self.GENERATED

    @property
    def EMPTY2(self):
        return self.EMPTY

    @property
    def KEY16(self):
        return fromBinaryToHex(self.KEY)

    @property
    def GENERATED16(self):
        return fromBinaryToHex(self.GENERATED)

    @property
    def EMPTY16(self):
        return fromBinaryToHex(self.EMPTY)

    @property
    def KEY(self):
        return fromBinaryToHex(self.KEY)

    @property
    def GENERATED(self):
        return fromBinaryToHex(self.GENERATED)

    @property
    def EMPTY(self):
        return fromBinaryToHex(self.EMPTY)


def tables(table):
    if (table == 'IP'):
        '''Used in the inital permutation'''

        IP = [58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7]

        return IP
    if (table == 'IIP'):
        IIP = [40, 8, 48, 16, 56, 24, 64, 32,
               39, 7, 47, 15, 55, 23, 63, 31,
               38, 6, 46, 14, 54, 22, 62, 30,
               37, 5, 45, 13, 53, 21, 61, 29,
               36, 4, 44, 12, 52, 20, 60, 28,
               35, 3, 43, 11, 51, 19, 59, 27,
               34, 2, 42, 10, 50, 18, 58, 26,
               33, 1, 41, 9, 49, 17, 57, 25]
        return IIP
    ''' Used in permutations.'''
    if (table == 'P'):
        P = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]
        return P
    '''Used in the key scheduling algorithms'''
    if (table == 'PCL'):
        PCL = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36]
        return PCL
    if (table == 'PCR'):
        PCR = [63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4]
        return PCR
    if (table == 'PC2'):
        PC2 = [14, 17, 11, 24, 1, 5,
               3, 28, 15, 6, 21, 10,
               23, 19, 12, 4, 26, 8,
               16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55,
               30, 40, 51, 45, 33, 48,
               44, 49, 39, 56, 34, 53,
               46, 42, 50, 36, 29, 32]
        return PC2
    if (table == 'EX'):
        '''Used in the expansiion from 32 bits to 64 bits.'''
        EXPANSION = \
            [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]
        return EXPANSION
    '''Used in the substitution layer'''
    if (table == 'S1'):
        S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
        return S1
    if (table == 'S2'):
        S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
        return S2
    if (table == 'S3'):
        S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
        return S3
    if (table == 'S4'):
        S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
        return S4
    if (table == 'S5'):
        S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
        return S5
    if (table == 'S6'):
        S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
        return S6

    if (table == 'S7'):
        S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
        return S7
    if (table == 'S8'):
        S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        return S8


def getShiftAmmount(round, flag):
    if ((round == 1 and flag == 1) or round == 2 or round == 9 or round == 16):
        return 1
    if flag == -1 and round == 1:
        return 0
    return 2


def getRandom_N(r):
    number = ""
    for i in range(r):
        number += str(random.randint(0, 1))
    return number


def roundShift(bits, round, flag):
    amount = getShiftAmmount(round, flag) % len(bits)
    return bits[flag * amount:] + bits[:flag * amount]


def setBits(bits, table):
    n = len(table)
    newbits = ""
    for i in range(n):
        newbits += bits[table[i] - 1]
    return newbits


def expansion(bits):
    if (len(bits) != 32):
        raise Exception('Not the right length (32)')
    return setBits(bits, tables("EX"))


def initial_permutation(bits):
    if (len(bits) != len(tables('IP'))):
        raise Exception('Cant make the permutatioion IP because they are different lengths.')
    if (len(bits) != 64):
        raise Exception('Not the right length (64).')
    return setBits(bits, tables('IP'))


def inverse_initial_permutation(bits):
    if (len(bits) != len(tables('IIP'))):
        raise Exception('Cant make the permutatioion IP because they are different lengths.')
    if (len(bits) != 64):
        raise Exception('Not the right length (64).')
    return setBits(bits, tables('IIP'))


def xor(bits, key, num):
    if (len(bits) != len(key)):
        raise Exception("Can`t XOR if they are different lengths")
    return paddWord(str(bin(int(bits, 2) ^ int(key, 2))).split('b')[1], num)


def setSbox(bits, table):
    return tables(table)[int(bits[0] + bits[5], 2)][int(bits[1:5], 2)]


def s_boxes(bits):
    if (len(bits) != 48):
        raise Exception('Can`t do s boxes, not the same length')
    newbits = ""
    for i in range(8):
        word = str(bin(setSbox(bits[6 * i:6 * i + 6], f'S{i + 1}'))).split('b')[1]
        if (len(word) != 4):
            word = paddWord(word, 4)
        newbits += word
    return newbits


def paddWord(word, n):
    while (len(word) != n):
        word = '0' + word
    return word


def perumtation(word):
    return setBits(word, tables('P'))


def feistel(r, key):
    if (len(r) != 32):
        raise Exception('Right side is not 32')
    if (len(key) != 48):
        raise Exception('Key is not 48')
    r = expansion(r)
    r = xor(r, key, 48)
    r = s_boxes(r)
    a = perumtation(r)
    return a


def generateKeys(key):
    if (len(key) != 64):
        raise Exception('Key not adequate length (64)')
    keys = []
    l, r = setBits(key, tables('PCL')), setBits(key, tables('PCR'))
    for i in range(16):
        l, r = roundShift(l, i + 1, 1), roundShift(r, i + 1, 1)
        keys.append(setBits(l + r, tables('PC2')))
    return keys


def encode(pt, key):
    if (len(pt) != 64):
        raise Exception('Plain text is not of 64 length')
    if (len(key) != 64):
        raise Exception('Key not adequate length (64)')
    pt = initial_permutation(pt)
    keys = generateKeys(key)
    for i in range(16):
        l, r = pt[:32], pt[32:]
        b = xor(l, feistel(r, keys[i]), 32)
        pt = r + b
    return inverse_initial_permutation(pt[32:] + pt[:32])


def decode(pt, key):
    if (len(pt) != 64):
        raise Exception('Plain text is not of 64 length')
    if (len(key) != 64):
        raise Exception('Key not adequate length (64)')
    pt = initial_permutation(pt)
    keys = generateKeys(key)
    for i in range(16):
        l, r = pt[:32], pt[32:]
        b = xor(l, feistel(r, keys[15 - i]), 32)
        pt = r + b
    return inverse_initial_permutation(pt[32:] + pt[:32])


def typeOfKey(key):
    WK = ['0101010101010101', 'FEFEFEFEFEFEFEFE ', 'E0E0E0E0F1F1F1F1', '1F1F1F1F0E0E0E0E']
    SWK = ['011F011F010E010E', '1F011F010E010E01', '01E001E001F101F1', 'E001E001F101F101',
           '01FE01FE01FE01FE', 'FE01FE01FE01FE01', '1FE01FE00EF10EF1', 'E01FE01FF10EF10E',
           '1FFE1FFE0EFE0EFE', 'FE1FFE1FFE0EFE0E', 'E0FEE0FEF1FEF1FE', 'FEE0FEE0FEF1FEF1']
    PWK = ['01011F1F01010E0E', '1F1F01010E0E0101', 'E0E01F1FF1F10E0E', '0101E0E00101F1F1',
           '1F1FE0E00E0EF1F1', 'E0E0FEFEF1F1FEFE', '0101FEFE0101FEFE', '1F1FFEFE0E0EFEFE',
           'E0FE011FF1FE010E', '011F1F01010E0E01', '1FE001FE0EF101FE', 'E0FE1F01F1FE0E01',
           '011FE0FE010EF1FE', '1FE0E01F0EF1F10E', 'E0FEFEE0F1FEFEF1', '011FFEE0010EFEF1',
           '1FE0FE010EF1FE01', 'FE0101FEFE0101FE', '01E01FFE01F10EFE', '1FFE01E00EFE01F1',
           'FE011FE0FE010EF1', 'FE01E01FFE01F10E', '1FFEE0010EFEF101', 'FE1F01E0FE0E01F1',
           '01E0E00101F1F101', '1FFEFE1F0EFEFE0E', 'FE1FE001FE0EF101', '01E0FE1F01F1FE0E',
           'E00101E0F10101F1', 'FE1F1FFEFE0E0EFE', '01FE1FE001FE0EF1', 'E0011FFEF1010EFE',
           'FEE0011FFEF1010E', '01FEE01F01FEF10E', 'E001FE1FF101FE0E', 'FEE01F01FEF10E01',
           '01FEFE0101FEFE01', 'E01F01FEF10E01FE', 'FEE0E0FEFEF1F1FE', '1F01011F0E01010E',
           'E01F1FE0F10E0EF1', 'FEFE0101FEFE0101', '1F01E0FE0E01F1FE', 'E01FFE01F10EFE01',
           'FEFE1F1FFEFE0E0E', '1F01FEE00E01FEF1', 'E0E00101F1F10101', 'FEFEE0E0FEFEF1F1']

    for w in WK:
        if w == key:
            return 'Weak'
    for w in SWK:
        if w == key:
            return 'Semi Weak'
    for w in PWK:
        if w == key:
            return 'Possible Weak'
    return 'Normal '


def fromBinaryToHex(bits):
    return str(hex(int(bits, 2))).split('x')[1].upper()


def fromHexToBinary(hex):
    return str(bin(int(hex, 16))).split('b')[1]


def fromDecToHex(dec):
    return str(hex(dec)).split('x')[1]


def fromBinaryToDec(bits):
    return str(int(bits, 2))


def fromDecToBinary(dec):
    return str(bin(dec)).split('b')[1]


def fromHexToDec(hex):
    return str(int(hex, 16)).split('x')[1]


def generateEmptyString():
    new = ''
    for i in range(64):
        new += '0'
    return new




def simulate_weak_keys():
    print(f'The block cipher DES has a few specific keys termed "weak keys" and "semi-weak keys". These are keys that cause the encryption mode of DES to act identically to the decryption mode of DES (albeit potentially that of a different key).')


def simulate100EncodingsAndDecodings():
    c = 0
    for i in range(100):
        text = getRandom_N(64)
        key = getRandom_N(64)
        encoded = encode(text, key)
        decoded = decode(encoded, key)
        if decoded == text:
            c += 1
    print(f'From 100 random generated keys and plaintexts, we have correctly encoded and decoded {c}')


if __name__ == "__main__":
    const=Constants()

    simulate_weak_keys()