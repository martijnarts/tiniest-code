#!/usr/bin/env python3
def shift(string, key, decipher=False):
    return ''.join(
        chr((ord(c) & 224)+(ord(c) % 32-1-key*(2*decipher-1)*c.isalpha()) %
            26+1) for c in string)


if __name__ == '__main__':
    assert shift('abcz+', 1) == 'bcda+', shift('abcz+', 1)
    assert shift('ABCZ+', 1) == 'BCDA+', shift('ABCZ+', 1)
    assert shift('bcda+', 1, True) == 'abcz+', shift('bcda+', 1, True)
