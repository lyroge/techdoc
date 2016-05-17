# -*- coding: UTF-8 -*-
"""
冒泡排序原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
将元素两两比较，最大（小）的放到一端
"""

import random


def bubble_sort(arg):
    arg_len = len(arg)
    for i in range(arg_len - 1):
        for j in range(i + 1, arg_len):
            if arg[i] > arg[j]:
                arg[i], arg[j] = arg[j], arg[i]


if __name__ == "__main__":
    test_ary = range(50)
    random.shuffle(test_ary)
    print test_ary
    bubble_sort(test_ary)
    print test_ary
