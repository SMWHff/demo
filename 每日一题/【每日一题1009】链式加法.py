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


class AddChain:
    """
    链式加法类
    """
    data = 0

    # 实例化类时触发，并获取实例化参数
    def __init__(self, n: int):
        self.data += n

    # 使用 == 比较时触发， other 为等号右边的值
    def __eq__(self, other):
        return self.data == other

    # 被调用时触发，返回自身，实现无限链式调用
    def __call__(self, n: int):
        self.data += n
        return self


def add_chain(n: int):
    return AddChain(n)


assert add_chain(1) == 1
assert add_chain(1)(2) == 3
assert add_chain(1)(2)(3) == 6
assert add_chain(1)(2)(3)(4) == 10
