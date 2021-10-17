# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题1014】退格字符串.py
# @Time       : 2021/10/15 1:48

"""
假设字符串中的”#“符号表示的是一个退格(删除)，例如在字符串"a#bc#d"其实最终结果是"bd"。请编写一个函数，接收一个含有退格符号的字符串，输出退格后的最终结果。

示例：
输入：" abc#d##c"，输出：“ac”
输入：“abc##d######”，输出：""
题目难度：简单
题目来源：codewars : Backspaces in string 2
"""


def backspace_str(word: str) -> str:
    # 获取整个字符串的长度
    len_word = len(word)
    # 通过删除所有 # 字符
    # 获取字符串中所有字母的长度
    len_str = len(word.replace("#", ""))
    # 【特殊情况】如果字母的长度未超过整个字符串长度的一半，则直接返回空字符
    if len_str <= len_word / 2:
        return ""
    # 定义储存字母索引的列表
    list_index = []
    # 将整个字符串转为列表
    list_word = list(word)
    # 遍历字符串列表
    for i in range(len_word):
        if list_word[i] == "#":
            # 该字符为 # 则将自身置为空字符
            list_word[i] = ""
            # 取左边离 # 字符最近的一位字母索引
            j = list_index[-1]
            # 将该字母置为空字符
            list_word[j] = ""
            # 然后已被删除的字母索引也从索引列表中删除
            list_index[-1:] = []
        else:
            # 将字母的索引放入索引储存列表中
            list_index.append(i)
    # 将处理后的列表转回为字符串
    return "".join(list_word)


assert backspace_str("a#bc#d") == "bd"
assert backspace_str("abc#d##c") == "ac"
assert backspace_str("abc##d######") == ""
