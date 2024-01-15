#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib(n, variant=0):
    def fib_td(n):
        if n <= 1:
            f[n] = n
        else:
            f[n] = fib_td(n - 1) + fib_td(n-2)
        return f[n]

    def fib_bu(n):
        f = [-1] * (n+1)
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
            
        return f[n]

    def fib_bu_imroved(n):
        if n <= 1:
            return n
        
        first, second = 0, 1

        for _ in range(n - 1):
            first, second = second, first + second

        return second

    match variant:
        case 0:
            f = [-1]*(n+1)
            return fib_td(n)
        case 1:
            return fib_bu(n)
        case 2:
            return fib_bu_imroved(n)
        case _:
            print(f"Ошибка")


if __name__ == '__main__':
    print(f"fib(15, 0) = {fib(15, 0)}")
    print(f"fib(15, 0) = {fib(15, 1)}")
    print(f"fib(15, 0) = {fib(15, 2)}")