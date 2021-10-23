# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题0928】魔方比赛成绩.py
# @Time       : 2021/10/23 19:25


"""
在大部分的魔方速拧比赛中，会记录一个选手的5次成绩，平均成绩的方式为去掉最高分和最低分后的平均分。请编写一个函数，给定一个包含5个浮点数的成绩列表times，求出他的平均成绩和最佳成绩（最多保留2位小数）。

示例：
输入： [9.5, 7.6, 11.4, 10.5, 8.1]，输出： (9.37, 7.6)。
因为平均成绩是：(9.5 + 10.5 + 8.1) / 3 = 9.37，最佳成绩是：7.6。

题目难度：简单
题目来源：codewars 2
"""


def cube_times(times: list) -> tuple:
    # 获取列表长度
    n = len(times)-1
    m = n
    # 用冒泡算法排序
    for i in range(0, n):
        for j in range(0, m):
            if times[j] > times[j+1]:
                times[j], times[j + 1] = times[j + 1], times[j]
        # 优化冒泡算法代码
        m = m - 1
    # 计算掐头去尾的平均值，返回两位小数
    avg = round(sum(times[1:-1])/(len(times)-2), 2)
    # 获取最佳成绩
    min = times[0]
    # 返回元组（平均成绩，最佳成绩）
    return (avg, min)


assert cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) == (9.37, 7.6)
assert cube_times([13.4, 12.3, 9.5, 11.9, 20.8]) == (12.53, 9.5)
assert cube_times([28.3, 14.5, 17.3, 8.9, 10.1]) == (13.97, 8.9)
