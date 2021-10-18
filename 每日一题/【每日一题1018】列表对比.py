# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1018】列表对比.py
# @Time       : 2021/10/18 21:37


"""
给定两个数字列表a 和 b，请编写一个函数list_diff(a, b)，将列表a中的同时也在b列表中出现的元素移除，并且保留原有的位置顺序。函数返回对比后的列表。
示例：
输入：a=[1,2], b=[1]，输出：[2]
输入：a=[1,2,2,2,3], b=[2]，输出：[1, 3]
题目难度：中等
题目来源：codewars： Array.diff 3
"""


def list_diff(a: list, b: list) ->list:
    # 将列表a转化为集合
    set_a = set(a)
    # 将列表b转化为集合
    set_b = set(b)
    # 进行a集合与b集合的差集运算
    set_result = set_a.difference(set_b)
    # 由于转成集合会导致去除重复元素
    # 需要在列表a中遍历出差集中的所有元素，返回列表
    result = [v for v in a+b if v in set_result ]
    return result

assert list_diff([1,2], [1]) == [2]
assert list_diff([1,2,2], [1]) == [2,2]
assert list_diff([1,2,2,2,3], [2]) == [1,3]

