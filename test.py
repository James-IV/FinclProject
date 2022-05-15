from cgitb import small
from copy import copy
from email import message
from logging import NullHandler
import math
from mimetypes import init
from token import EQUAL
import bitarray
from bitarray.util import ba2int
import random

from pip import main

Big_PrimeTable = {0: 499, 1: 383, 2: 937, 3: 1069,
                  4: 811, 5: 643, 6: 151, 7: 97, 8: 89, 9: 43, 10: 23, 11: 733, 12: 179, 13: 11, 14: 31, 15: 43}
Small_PrimeTable = {0: 29, 1: 5, 2: 7, 3: 11,
                    4: 13, 5: 17, 6: 19, 7: 23}
replace_Cipher = []
a = bitarray.bitarray()
with open('test.m4a', 'rb') as fh:
    a.fromfile(fh)
print(len(a), ' len')
start = int(len(a)/2-3*math.sqrt(len(a)))
end = int(len(a)/2+3*math.sqrt(len(a)))
N = random.randint(3, 10)

iniKey = a[start:end]
p = len(iniKey)/N
for i in range(1, int(N/2)):
    iniKey[i*2*p-p:i*2*p] = bitarray.reverse(iniKey[i*2*p-p:i*2*p])
#key = iniKey
for i in range(1, N-1):
    key = iniKey[i*p-p:i*p] ^ iniKey[i*p:i*p+p]
    # seq = a[0:-1]
    #
    # print(seq)


def Message_Encoder(msg):
    msg = bitarray.bitarray(
        '0010001001011101010101000011101001010010111100011110010011100')
    msg_len = len(msg)
    minum = 0
    maxum = 0
    if msg_len <= 1000:
        frist_choice = int(msg_len/3)
        last_choice = int(msg_len*4/5)
        choose2 = ba2int(msg[last_choice:last_choice+2])
        choose1 = ba2int(msg[frist_choice:frist_choice+2])
        print(choose1, choose2)
        if choose1 > choose2:
            maxum = Small_PrimeTable[choose2]
            minum = Small_PrimeTable[choose1]
        elif choose1 == choose2:
            maxum = Small_PrimeTable[choose2]
            minum = Small_PrimeTable[(choose1+1) % 8]
        else:
            maxum = Small_PrimeTable[choose1]
            minum = Small_PrimeTable[choose2]
        shift_Num = ba2int(msg[-10:0]) % maxum
        index = shift_Num
        replace_Cipher.append(shift_Num)
        for i in range(maxum-1):
            index = (index+minum) % maxum
            replace_Cipher.append(index)
        print(replace_Cipher)

    else:
        return 0
    return msg


# combine part 1 ciphertext and part 2 key
def Key_XOR(ciphertext, key):
    # AES(ciphertext,key)
    from itertools import cycle
    encrypt_result = bitarray('')
    text_len = len(ciphertext)
    key_len = len(key)
    key_cycle = cycle(key)
    for idx in range(0, text_len):
        encrypt_result.append(ciphertext[idx] ^ next(key_cycle))

    return encrypt_result


if __name__ == '__main__':
    Message_Encoder(b'0')
