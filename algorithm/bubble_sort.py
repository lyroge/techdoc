# -*- coding: UTF-8 -*-
"""
快速排序原理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
选择一个值，然后将大于和小于他的值划分为两部分，然后递归对每个划分的集合再进行操作
直到每一个集合都只有一个元素位置
"""

import random


def quick_sort(ary, start=0, end=0):
    # 结束递归条件为元素个数小于1
    if end - start <= 1:
        return

    # 选择第一个值为对比元素
    index = start
    flag_value = ary[start]
    len_ls = end - start

    # 将小于他的值放入他的左边
    for i in range(start+1, end):
        if ary[i] < flag_value:
            min_v = ary.pop(i)
            ary.insert(0, min_v)

    # 找到标志值位置，然后划分两部分
    index = ary.index(flag_value)
    print index
    quick_sort(ary, 0, index + 1)
    quick_sort(ary, index + 1, len_ls)


if __name__ == "__main__":
    test_ary = range(50)
    random.shuffle(test_ary)
    print test_ary
    quick_sort(test_ary, 0, len(test_ary))
    print test_ary
