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
        if not choose2 == choose1:
            maxum = Small_PrimeTable[choose2]
            minum = Small_PrimeTable[choose1]
        else:
            maxum = Small_PrimeTable[choose2]
            maxum = Small_PrimeTable[(choose2+1) % 8]
        if maxum < minum:
            tmp = minum
            minum = maxum
            maxum = tmp
        shift_Num = ba2int(msg[-10:]) % maxum
        Create_Replace_Cipher(shift_Num, minum, maxum)
        renew = Enctypt_plainText(msg)
        fin = Decrypt_plainText(renew)
    else:
        return 0
    return msg


def Create_Replace_Cipher(shift_Num, MultiplyPrime, ModPrime):
    index = shift_Num
    replace_Cipher.append(shift_Num)
    for i in range(ModPrime-1):
        index = (index+MultiplyPrime) % ModPrime
        replace_Cipher.append(index)
    print(replace_Cipher)


def Enctypt_plainText(msg):
    ModPrime = len(replace_Cipher)
    slice_N = int(len(msg)/ModPrime)
    print(slice_N, len(msg), ModPrime)
    renew = bitarray.bitarray(len(msg))
    for i in range(slice_N):
        for j in range(ModPrime):
            renew[i*ModPrime+j] = msg[i*ModPrime+replace_Cipher[j]]
    for i in range(len(msg) % ModPrime):
        renew[i+slice_N*ModPrime] = msg[len(msg)-i-1]
    print('msgbefore:', msg)
    print('msgafter:', renew)
    return renew


def Decrypt_plainText(msg):
    ModPrime = len(replace_Cipher)
    slice_N = int(len(msg)/ModPrime)
    print(slice_N, len(msg), ModPrime)
    recover = bitarray.bitarray(len(msg))
    for i in range(slice_N):
        for j in range(ModPrime):
            recover[i*ModPrime+replace_Cipher[j]] = msg[i*ModPrime+j]
    for i in range(len(msg) % ModPrime):
        recover[i+slice_N*ModPrime] = msg[len(msg)-i-1]
    print('msgbefore:', msg)
    print('msgdecrypt:', recover)
    return recover


if __name__ == '__main__':
    Message_Encoder(b'0')
