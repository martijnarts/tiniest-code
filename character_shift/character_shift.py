#!/usr/bin/env python3
def shift(string, key, decipher=False):
    return ''.join(
        chr((ord(c.upper())-65+key*(1-2*decipher)) % 26+65+32*c.islower())
        if c.isalpha() else c for c in string)

if __name__ == '__main__':
    assert shift('abcz+', 1) == 'bcda+', shift('abcz+', 1)
    assert shift('ABCZ+', 1) == 'BCDA+', shift('ABCZ+', 1)
    assert shift('bcda+', 1, True) == 'abcz+', shift('bcda+', 1, True)
