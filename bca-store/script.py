#!/usr/bin/python3
import sys

def count_change(s):
    a, b, c, d = 0,0,0,0
    s = s.split(' ')
    money = int(s[-1])

    for i in s:
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
        elif i == 'D':
            d += 1

    pa = a * 45
    pb = b * 52
    pc = c * 67
    pd = d * 75

    db = ((10/100)*52)*(b//2)
    dc = ((50/100)*67)*(c//2)
    dd = (d//3)*75

    ht = (pa+pb+pc+pd)-(db+dc+dd)

    if money >= ht:
        change = money-ht
        return "%.2f" % change
    else:
        return "%i" % -1

    # print("a=%i, harga=%f" % (a,pa))
    # print("b=%i, harga=%f" % (b, (pb-db)))
    # print("c=%i, harga=%f" % (c, (pc-dc)))
    # print("d=%i, harga=%f" % (d, (pd-dd)))
    # print("harga total=%f" % ht)
    # print("kembalian=%f" % change)

def main():
    raw_input = sys.stdin.read()
    input = raw_input.split('\n')

    output = []

    for s in input:
        if s is not '':
            output.append(count_change(s))

    print(' '.join(output))

if __name__ == '__main__':
    main()
