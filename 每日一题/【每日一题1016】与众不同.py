# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1016】与众不同.py
# @Time       : 2021/10/17 11:57


"""
给定一个由正整数组成的列表，其中有且仅有一个与其他元素都不相同的数字，请编写一个函数，找出这个与众不同的数字。列表元素总个数是奇数个。

示例：
输入：[1, 1, 2]，输出，2
输入： [17, 17, 3, 17, 17, 17, 17]，输出：3

题目难度：简单
题目来源：codewars : Find the stray number
"""


def find_stray(nums: list) -> int:
    # 定义一个计数字典
    dict_count = dict()
    # 遍历列表中的每个数字，并统计出现次数
    for num in nums:
        # 获取该数字之前在计数字典中统计的次数
        # 如果没有被统计过则设置初始值为 0
        count = dict_count.get(num, 0)
        # 该数字统计次数 +1
        dict_count[num] = count + 1
    # 在计数字典中找出只出现一次的数字
    for k in dict_count:
        if dict_count[k] == 1:
            return k


assert find_stray([1, 1, 1, 1, 1, 1, 2]) == 2
assert find_stray([2, 3, 2, 2, 2]) == 3
assert find_stray([3, 2, 2, 2, 2]) == 3
