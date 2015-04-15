#!/usr/bin/env python3
def shift(string, key, decipher=False):
    return ''.join(
        chr((ord(x) & 224)+((ord(x) & 31)-2*decipher) % 26+1)
        if ord(x) & 64 else x for x in string)

if __name__ == '__main__':
    assert shift('abcz+', 1) == 'bcda+', shift('abcz+', 1)
    assert shift('ABCZ+', 1) == 'BCDA+', shift('ABCZ+', 1)
    assert shift('bcda+', 1, True) == 'abcz+', shift('bcda+', 1, True)
