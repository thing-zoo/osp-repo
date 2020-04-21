#!/usr/bin/python
import my_pkg

while True:
    choice = int(input('Select menu: 1)conversion 2) union/intersection 3)exit ? '))
    
    if choice == 1:
        num = input('input binary number :')
        d = my_pkg.toDec(num)
        o = my_pkg.toOther(d, 8)
        h = my_pkg.toOther(d, 16)
        print('=> OCT> ', o)
        print('=> DEC> ', d)
        print('=> HEX> ', h)
    elif choice == 2:
        a = input('1st list : ').strip('[]').replace(',',' ').split()
        b = input('2st list : ').strip('[]').replace(',', ' ').split()
        u = my_pkg.union(a, b)
        i = my_pkg.inter(a, b)

        print('=> union [', end='')
        print(','.join(u), end =']\n')
        print('=> intersection [',end ='')
        print(','.join(i), end=']\n')
    else :
        print('exit the program')
        exit()
