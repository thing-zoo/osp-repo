#!/usr/bin/python

def union(*ar):
    u = []
    for item in ar:
        for x in item:
            if x not in u:
                u.append(x)
    u.sort()            
    return u

def inter(a, b):
    i = []
    for x in a:
        if x in b:
            i.append(x)
    i.sort()
    return i
