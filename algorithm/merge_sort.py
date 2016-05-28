# -*- coding: UTF-8 -*-
"""
归并排序算法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
归并排序原理就是将数组分为2个排好序的数组，然后“合”在一起
因为一个元素的数组肯定是排好序的，所以递归后主要在合并
"""

import random


def merge_sort(ary, start, end):
    if end - start <= 1:
        return

    # 先将数组分开
    mid = (end - start) / 2

    merge_sort(ary, start, start + mid)
    merge_sort(ary, start + mid, end)

    # 再将数组合并
    ary1 = ary[start:start + mid]
    ary2 = ary[start + mid:end]

    new_ary = []

    i, j = 0, 0
    while True:
        if i >= len(ary1) or j >= len(ary2):
            break

        if ary1[i] < ary2[j]:
            new_ary.append(ary1[i])
            i += 1
        else:
            new_ary.append(ary2[j])
            j += 1

    if i < len(ary1):
        new_ary.extend(ary1[i:])

    if j < len(ary2):
        new_ary.extend(ary2[j:])

    ary[start:end] = new_ary

if __name__ == '__main__':
    array = range(200)
    random.shuffle(array)
    print array
    merge_sort(array, 0, len(array))
    print array
