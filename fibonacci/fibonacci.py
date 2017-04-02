#!/usr/bin/env python3
def fib(n):
    return fib(n-1)+[sum(fib(n-1)[-2:])]if n > 2 else[1]*n


if __name__ == '__main__':
    assert fib(0) == [], fib(0)
    assert fib(1) == [1], fib(1)
    assert fib(5) == [1, 1, 2, 3, 5], fib(5)
    assert fib(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], fib(10)
