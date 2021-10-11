# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1009】链式加法.py
# @Time       : 2021/10/9 15:55

"""
我们的任务是编写一个加法函数add()，接收纯数字作为参数，并且可以实现一个有趣的链式加法，也就是如果我们调用add(1)(2)(3)可以得到6。

示例：
输入： add(1)，返回：1
输入： add(1)(2)(3)，返回：6

题目难度：中等
题目来源：codewars 14
"""


class add_chain(int):
    def __call__(self, n: int):
        return add_chain(self + n)

assert add_chain(1) == 1
assert add_chain(1)(2) == 3
assert add_chain(1)(2)(3) == 6
assert add_chain(1)(2)(3)(6) == 12
assert add_chain(1)(2)(3) + 10 == 16

