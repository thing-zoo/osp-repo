#!/usr/bin/python

def fibo(n):
    if n < 2 : return n

    return fibo(n-1) + fibo(n-2)

n = int(input("fibonacci number?: "))

for i in range(1, n):
    print(fibo(i), end = ",")

print(fibo(n))
print("F%d = %d" %(n, fibo(n)))

