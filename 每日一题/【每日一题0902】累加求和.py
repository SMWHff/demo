# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题0902】累加求和.py
# @Time       : 2021/9/4 13:03


"""
给定一个正整数，请编写一个python函数，将它的字面数字进行累加总和，并列出算式。例如1234 ，那么返回1 + 2 + 3 + 4 = 10 。

题目难度：简单
题目来源：codewars 6
"""

def sum_of_digits(num: int) -> str:
    list_num = list(str(num))
    result = sum([int(i) for i in list_num])
    str_num = f"{' + '.join(list_num)} = {result}"
    return str_num

assert sum_of_digits(1234) == "1 + 2 + 3 + 4 = 10"
assert sum_of_digits(64323) == "6 + 4 + 3 + 2 + 3 = 18"
assert sum_of_digits(8) == "8 = 8"