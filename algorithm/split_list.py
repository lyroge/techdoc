# -*- coding: UTF-8 -*-
"""
将数据划分为两部分
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一部分大于第一个数字、一部分小于第一个数字
"""


import random


def split_list(ls):
    # 标记值位置及值
    flag_index = 0
    flag_value = ls[flag_index]

    # 标记是否发生改变，无改变则结束
    happend_change = True
    while happend_change:
        i = flag_index + 1
        while i < len(ls):
            # 如果发现比flag_value小的值，那么则交换然后进行下一次比较
            if ls[i] < flag_value:
                ls[flag_index] = ls[i]
                flag_index += 1
                ls[i] = ls[flag_index]
                happend_change = True
                break
            else:
                happend_change = False
                i += 1
    ls[flag_index] = flag_value


if __name__ == "__main__":
    ls = range(100)
    random.shuffle(ls)
    print ls
    split_list(ls)
    print ls
