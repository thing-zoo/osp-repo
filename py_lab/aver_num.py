#!/usr/bin/python

n = int(input("Enter the number to compute average: "))

total = 0

for i in range(0, n):
    total += int(input("Enter the number: "))

aver = total/n

print("average:", aver)
