# -*- coding:utf-8 -*-

import collections

def main():
    a = "GAGGAGTATTGACAGGAGGACATAGCTCCGATCCCGGTAGCATTACTTTTGCGCACGCTTATCAATTCTTCCTGCCCGTAATGAGTAGGCGCGCGCGGGATCATTGGGCCACCGACAAGAGCTCACCGGATGGGTGTGCCCATCTTGAACATCGAAGAAGCTAAGAAAACCACAACAGACCTCATTTATAATTCAAGCCAACCAACAATCATTATCGCACCCCCTCGGGAGGCCGATGGCTGGCCAACCCGCTAAGCCTGGTGTCCAACCCCTAATGTCAAAGCCGTGCCGCCACAGTGCCTTCGCCTAGCGCTGACATCATTCAGAAGGAAGAGCCCTGCGCGTTTTTAAACCAGCAGGGGTATGGATAGCGAGGGGGTCATCCTTGGAATGCAACTCTGACGGTGTGCGCCGATTGGATGACAGAGATATAACGTCACAGACCGAGTTATTGCTTGTCGATCTAGGGTTCCGGGTAAGTCTTTGTAGGGATTCCGCCAGAGGGCTCCACTCCCATCTCCGGTCATGACGCTCACGAATGGCCTCGGTGGGGTTTCCTTCGTGCGATTGTACATGGGATTTAAAGGCGAGTTCATCCAAACTCATCTCTTGTCTACACTAGGTCTATGATAGAGTATTGGCTGCCCACCAAGAAGTCTAGTTGACAATTGTAACCTTTGTTGTTTTCCCTACACCATACAAGCGACGGCTATTGACAACGAAACGTCCGGTTTTCATGCGAATCTCACCCCATCTTTATCCCCAGCGGTGTCCTATCGCCCACGGAGAATTTCGCAAAGTGCTTCCAGACACAATCAGCTTATGCCTTCCATTTGTGGATGTTCGGTGTGGCTTTAACGAGGCCCGA"
    obj = collections.Counter(a)
    print(obj)
    r = []
    for i in ['A','C','G','T']:
        r.append(obj[i])
        print(obj[i])

if __name__ == "__main__":
    main()