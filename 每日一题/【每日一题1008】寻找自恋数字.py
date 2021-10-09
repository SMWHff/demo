# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1008】寻找自恋数字.py
# @Time       : 2021/10/8 12:16


"""
「自恋数字」表示的是一个正整数，它的字面值刚好等于其每个组成数字按照总个数的幂次方的总和。给定一个数字，请编写一个函数判断它是否是“自恋数字”。
示例：
输入：153，输出：True。
解析：因为它一共由1,5,3这3个数字组成，1^3 + 5^3 +3^3 = 1+125+27 = 153。

题目难度：简单
题目来源：codewars 8
"""


def narcissistic(num: int) -> bool:
    # 获取数字总个数
    n = len(str(num))
    # 将每个数字按照数字总个数的幂次方进行运算
    list_num = [int(v)**n for v in str(num)]
    # 计算列表所有元素的总和
    sum_num = sum(list_num)
    # 将计算的总和与传入的数字对比
    # 相等则为「自恋数字」
    return sum_num == num

assert narcissistic(7) is True
assert narcissistic(371) is True
assert narcissistic(122) is False
assert narcissistic(4887) is False