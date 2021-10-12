# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1011】奇偶比较.py
# @Time       : 2021/10/11 21:04


"""
给定一个数字，请编写一个函数，判断其中组成数字中，比较所有的奇数和偶数的总和，如果奇数总和大于等于偶数总和则返回True，否则返回False。

示例：
输入：12，输出：False
输入：123，输出：True

题目难度：简单
题目来源：codewars 5
"""


def odd_or_even(n: int) -> bool:
    # 定义奇数和变量，初始值为 0
    odd_sum = 0
    # 定义偶数和变量，初始值为 0
    even_sum = 0
    # 转化为字符串，遍历每一位字符
    for v in str(n):
        # 将单个字符再转化为数值
        num = int(v)
        # 判断是否为偶数
        # 可以被 2 整除的数则为偶数
        if num % 2 == 0:
            # 数值与偶数和进行累加
            even_sum += num
        else:
            # 数值与奇数和进行累加
            odd_sum += num
    # 返回奇数总和大于等于偶数总和的比较
    return odd_sum >= even_sum

assert odd_or_even(12) is False
assert odd_or_even(123) is True
assert odd_or_even(112) is True