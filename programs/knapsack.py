#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack_bu(W, weight, cell):
    def knapsack_with_reps(W, weight, cell):
        d = [0] * (W+1)

        for w in range(1, W+1):
            for weight_i, cell_i in zip(weight, cell):
                if weight_i <= w:
                    d[w] = max(d[w], d[w - weight_i] + cell_i)

        return d[W]

    def knapsack_without_reps(W, weight, cell):
        def restore(d, weight_rev, cell_rev):
            result = []
            w = W
            elem = len(weight_rev)

            for weight_i, cell_i in zip(weight_rev, cell_rev):
                if d[w][elem] == d[w - weight_i][elem-1] + cell_i:
                    result.append(1)
                    w -= weight_i

                else:
                    result.append(0)

                elem -= 1
            result.reverse()
            return result

        d = [[0] for _ in range(W+1)]
        d[0] = [0] * (len(weight) + 1)

        for weight_i, cell_i in zip(weight, cell):
            for w in range(1, W+1):
                d[w].append(d[w][-1])
                if weight_i <= w:
                    d[w][-1] = max(d[w][-1], d[w - weight_i][-2] + cell_i)

        result = restore(d, weight[::-1], cell[::-1])

        return d[W][-1], result

    with_rep = knapsack_with_reps(W, weight, cell)
    without_rep = knapsack_without_reps(W, weight, cell)

    return with_rep, without_rep


if __name__ == '__main__':
    W = 12
    weight = [8, 6, 4, 2]
    cell = [40, 10, 16, 9]
    with_rep_bu, without_rep_bu = knapsack_bu(W, weight, cell)
    print(f"weight = {weight}\ncell = {cell}\nРезультат:")
    print(f"with_rep_bu = {with_rep_bu}\nwithout_rep_bu = {without_rep_bu}")