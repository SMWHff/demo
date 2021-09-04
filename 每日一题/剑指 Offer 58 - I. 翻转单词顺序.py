# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 剑指 Offer 58 - I. 翻转单词顺序.py
# @Time       : 2021/9/4 12:31

def reverseWords(s: str) -> str:
    # 去除首尾多余空格
    s = s.strip()
    # 将字符串用空格分割成列表
    list_s = s.split(" ")
    # 将列表元素反转
    list_s = list_s[::-1]
    # 去除列表内的空值元素
    list_s = [ x for x in list_s if x != '' ]
    # 将列表内元素用空格连接转化为字符串
    result = " ".join(list_s)
    # 返回字符串结果
    return result


assert reverseWords("the sky is blue") == "blue is sky the"
assert reverseWords("  hello world!  ") == "world! hello"
assert reverseWords("a good   example") == "example good a"