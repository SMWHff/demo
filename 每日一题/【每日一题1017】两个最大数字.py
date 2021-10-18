# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1017】两个最大数字.py
# @Time       : 2021/10/17 12:39


"""
给定一个数字列表，请编写一个函数，找出其中最大的两个不同数字，并且返回结果按照从大到小排列。

示例：
输入： [4, 10, 10, 9]，输出：[10, 9]
题目难度：简单
题目来源：codewars： Return Two Highest Values in List 1
"""


def two_highest(nums: list) -> list:
    # 定义最大值变量，初始值为空
    max_num = None
    # 定义第二大值变量，初始值为空
    second_num = None
    # 遍历列表中的每个数字
    for num in nums:
        # 判断最大值变量为空，则进行赋值操作
        # 或者该数字大于最大值，则进行赋值操作
        if max_num is None or num > max_num:
            max_num = num

        # 判断该数字小于最大值，则进入第二次判断
        if num < max_num:
            # 判断第二大值变量为空，则进行赋值操作
            # 或者该数字大于第二大值，则进行赋值操作
            if second_num is None or num > second_num:
                second_num = num

    # 最大值或者第二大值为空，则剔除掉
    # 然后返回列表
    result = [v for v in [max_num, second_num] if v]
    return result


assert two_highest([4, 10, 10, 9]) == [10, 9]
assert two_highest([15, 20, 20, 17]) == [20, 17]
assert two_highest([1, 1, 1]) == [1]
assert two_highest([]) == []
assert two_highest([52359, 86937, 63480, 43951, 26522, 14543, 97719, 75202, 17498, 76899, 38367, 6940, 52720, 71337, 57809, 98606, 827, 52453, 65904, 36280, 77386, 4433, 55644, 20134, 95284, 43207, 58752, 19164, 5214, 80570, 66083, 42417, 36423, 95450, 79775, 61809, 61856, 79566, 30627, 68128, 13701, 97031, 60769, 33254, 27015, 41398]) == [98606, 97031]
