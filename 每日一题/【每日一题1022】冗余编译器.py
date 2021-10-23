# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1022】冗余编译器.py
# @Time       : 2021/10/23 19:46


"""
给定一个字符串，请编写一个函数，检测其中的字符，如果只出现1次则编译成"("，如果出现多次则编译成")"。忽略字母的大小写。

示例
输入：" din"，输出：" ((("
输入：“Success”：，输出：" )())())"

题目难度：中等
题目来源：codewars: Duplicate Encoder 1
"""


def duplicate_encode(word: str) -> str:
    # 定义一个返回值变量
    result = ''
    # 忽略字母的大小写
    word = word.upper()
    # 遍历字符串中的每个字符
    for w in word:
        # 计算统计字符的出现次数
        count = word.count(w)
        if count > 1:
            # 出现多次则编译成")"
            result = result + ')'
        else:
            # 只出现1次则编译成"("
            result = result + '('
    # 返回编译后的字符串
    return result

assert duplicate_encode("din") == "((("
assert duplicate_encode("Success") == ")())())"
assert duplicate_encode("(( @") == "))(("