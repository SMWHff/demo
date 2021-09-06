# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题0906】数字间隔.py
# @Time       : 2021/9/6 12:17

"""
请编写一个函数，接收两个参数：一个是数字列表nums，一个是数字n。返回列表中任意两个数字的差值刚好是n的所有组合的个数。
示例：
输入：(nums=[1, 1, 5, 6, 9, 16, 27], n=4)，输出3。因为组合情况可以是：(1,5), (1,5), (5,9)

题目难度：简单
题目来源：codewars 5
"""


def int_diff(nums: list, n: int) -> int:
    # 定义匹配的组合个数
    group_count = 0
    # 第一层 for 循环
    for i in range(len(nums)):
        # 取第一个数
        num1 = nums[i]
        # 第二层 for 循环，以 i+1 开始
        for j in range(i + 1, len(nums)):
            # 取第二个数
            num2 = nums[j]
            # 判断两个数的差值是否为 n
            if abs(num2 - num1) == n:
                # 是则匹配的组合个数 +1
                group_count = group_count + 1
    # 返回匹配的组合个数
    return group_count

assert int_diff([1, 1, 5, 6, 9, 16, 27], 4) == 3
assert int_diff([1, 1, 3, 3], 2) == 4