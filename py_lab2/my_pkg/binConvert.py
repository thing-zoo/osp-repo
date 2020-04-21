#!/usr/bin/python

def convert2(num):
    num = int('0b'+ num, 2)

    print('=> OCT> ', format(num, 'o'))
    print('=> DEC> ', num)
    print('=> HEX> ', format(num, 'X'))

def toDec(n):
    #n is string (10101110)
    n = list(reversed(n))
    s = int(0)
    for i in range(len(n)):
        s += int(n[i])*(2**i)
    return s

def toOther(num, base):
    #num:10진수, base: 진수

    T = '0123456789ABCDEF'
    q, r = divmod(num, base)

    if q == 0:
        return T[r]
    else:
        return toOther(q, base)+T[r]
