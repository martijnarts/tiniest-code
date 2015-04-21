#!/usr/bin/env python3
def levenshtein(a, b):
    if (len(a) == 0):
        return len(b)
    if (len(b) == 0):
        return len(a)

    if (a[-1] == b[-1]):
        cost = 0
    else:
        cost = 1

    return min(levenshtein(a[:-1], b) + 1,
               levenshtein(a, b[:-1]) + 1,
               levenshtein(a[:-1], b[:-1]) + cost)

if __name__ == '__main__':
    assert levenshtein('cat', 'scent') == 3, levenshtein('cat', 'scent')
    assert levenshtein('back', 'book') == 2, levenshtein('back', 'book')
    assert levenshtein('rat', 'rat') == 0, levenshtein('rat', 'rat')
    assert levenshtein('barley', 'harry') == 3, levenshtein('barley', 'harry')
    assert levenshtein('+', '62') == 2, levenshtein('+', '62')
    assert levenshtein('plan', 'jupiter') == 6, levenshtein('plan', 'jupiter')
    assert levenshtein('', 'cake') == 4, levenshtein('', 'cake')
