#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_bottom_up(a):
    n = len(a)
    D = []

    for i in range(n):
        D.append(1)

        for j in range(i):
            if a[j] < a[i] and D[j] + 1 > D[i]:
                D[i] = D[j]+1

    ans = max(D)

    return ans


def using_prev(prev, m_index):
    result = []

    while True:
        result.append(m_index)

        if prev[m_index] == -1:
            break

        m_index = prev[m_index]

    result.reverse()
    return result


def without_prev(d, ans, m_index):
    result = []

    while True:
        result.append(m_index)

        if ans == 1:
            break
        ans -= 1

        while True:
            m_index -= 1
            if d[m_index] == ans and a[m_index] < a[result[-1]]:
                break

    result.reverse()
    return result


def list_bottom_up_2(a):
    n = len(a)
    d, prev = [], []
    
    for i in range(n):
        d.append(1)
        prev.append(-1)

        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j]+1
                prev[i] = j

    ans = 0
    max_index = 0
    for i, item in enumerate(d):
        if ans < item:
            ans, max_index = item, i

    list_using_prev = using_prev(prev, max_index)
    list_without_prev = without_prev(d, ans, max_index)

    return ans, (list_using_prev, list_without_prev)


if __name__ == '__main__':
    a = [4, 2, 1, 6, 8, 0, 8, 6, 3, 5, 6, 7, 4, 2, 5]
    print(list_bottom_up(a))
    print(list_bottom_up_2(a))