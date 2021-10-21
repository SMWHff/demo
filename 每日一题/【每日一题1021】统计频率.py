# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1021】统计频率.py
# @Time       : 2021/10/21 22:51


"""
给定一个字符串words和分隔符sep，请编写一个函数，统计字符串words中每个元素出现的次数，使用sep进行拼接。

示例：
输入：“hello world”，输出：" 1-1-3-3-2-1-1-2-1-3-1"

题目难度：简单
题目来源：codewars: Frequency sequence 1
"""

def freq_seq(words: str, sep: str) -> str:
    # 定义统计字典
    counts = {}
    # 将传入字符串转为列表
    result = list(words)
    # 遍历每个字符
    for s in words:
        # 统计每个字符次数
        counts[s] = counts.get(s,0) + 1
    # 遍历列表
    for i in range(len(words)):
        # 将每个字符替换成该字符统计的次数
        result[i] = str(counts[result[i]])
    # 通过分隔符将列表转为字符串
    return sep.join(result)


assert freq_seq("hello world", "-") == "1-1-3-3-2-1-1-2-1-3-1"
assert freq_seq("19999999", ":") == "1:7:7:7:7:7:7:7"
assert freq_seq("^^^**$", "x") == "3x3x3x2x2x1"