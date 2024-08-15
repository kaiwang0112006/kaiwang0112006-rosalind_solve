# -*- coding: utf-8 -*-
from collections import Counter

def main():
    with open("rosalind_conv.txt") as f:
        content = f.readlines()


    a = content[0].strip()
    b = content[1].strip()

    alist = [float(i) for i in a.split(" ")]
    blist = [float(i) for i in b.split(" ")]

    ab = []

    for i in alist:
        for j in blist:
            ab.append(round(i-j,5))

    cobj = dict(Counter(ab))
    maxcount = max(cobj.values())

    print(maxcount)
    for k in cobj:
        if cobj[k] == maxcount:
            print(k)
            break



if __name__ == "__main__":
    main()
