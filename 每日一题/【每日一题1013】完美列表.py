# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1013】完美列表.py
# @Time       : 2021/10/13 10:50

"""
一个完美列表是指，在这个列表中的每个数字n，其n-1或者n+1也存在于列表中。请编写一个函数，判断给定的列表是否是完美列表。

示例：
输入：[2, 10, 9, 3]，输出：True
解析：因为2=3-1，10=9+1，9=10-1，3=2+1，因此它是完美列表。

题目难度：简单
题目来源：codewars : Nice Array 2
"""


def is_nice(nums: list) -> bool:
    # 遍历列表中的每个数字
    for num in nums:
        if num - 1 in nums:
            # 数字-1 的结果存在列表中则通过进入下一轮
            pass
        elif num + 1 in nums:
            # 数字+1 的结果存在列表中则通过进入下一轮
            pass
        else:
            # 否则退出函数，直接返回 False
            return False
    # 列表中所有数字都符合则为完美列表，返回 True
    return True


assert is_nice([2, 10, 9, 3]) is True
assert is_nice([3, 4, 5, 7]) is False