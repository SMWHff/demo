# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1012】统计页码数字.py
# @Time       : 2021/10/12 14:20

"""
赫敏在一家印刷公司上班，她的一项工作就是统计一本书籍页码中包含的所有页码数字的个数（从1开始，包含结束页码）。比如，一本4页的书包含4个页码数字（1,2,3,4）。请编写一个函数，给定一个页数，求出一共出现的数字个数。

示例：
输入：4，输出：4。因为页数是1，2，3，4
输入：12，输出：15，因为1-9页共9个数字，10，11，12各有2各数字。

题目难度：简单
题目来源：codewars 8
"""


def page_digits(n: int) -> int:
    # 定义不同位数9的列表
    sizeTable = []
    for m in range(1, 20):
        sizeTable.append(int("9"*m))

    # 获取数字位数的方法
    def sizeOfInt(x: int):
        for i in range(len(sizeTable)):
            if x <= sizeTable[i]:
                return i+1
    # 获取传入数字的位数
    size = sizeOfInt(n)
    # 定义返回值
    result = None
    # 循环判断位数是否大于0
    while size > 0:
        if result is None:
            # 如果返回值未赋值，则进行首次赋值
            result = n * size
        else:
            # 返回值减去列表对应位数的9
            result = result - sizeTable[size-1]
        # 位数 -1
        size = size - 1
    return result


assert page_digits(4) == 4
assert page_digits(12) == 15
assert page_digits(100) == 192
assert page_digits(12345) == 50619
assert page_digits(12345678) == 87654321
assert page_digits(123456789) == 999999999
assert page_digits(400000000000000000) == 7088888888888888907
