# -*- coding: UTF-8 -*-
"""
快速排序原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
选择一个值，然后将大于和小于他的值划分为两部分，然后递归对每个划分的集合再进行操作
直到每一个集合都只有一个元素位置
"""

import random


def first_sort(array, low, high):
    key = array[low]
    while low < high:
        # 先处理最高上限的值降低到最小
        while low < high and array[high] >= key:
            high -= 1

        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = first_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


if __name__ == '__main__':
    array = range(100)
    random.shuffle(array)
    print array
    quick_sort(array, 0, len(array) - 1)
    print array
