# -*- coding: UTF-8 -*-
"""
插入排序原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
插入排序的原理在于如何的将值插入到合适位置
插入的办法是找到合适位置将数组元素统统后移
"""

import random


def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] <= array[j]:
                v = array[i]
                k = i
                while j < k:
                    array[k] = array[k-1]
                    k -= 1
                array[j] = v
                break

if __name__ == '__main__':
    array = range(100)
    random.shuffle(array)
    print array
    insert_sort(array)
    print array
