# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : 【每日一题0910】打字员.py
# @Time       : 2021/9/10 21:29


"""
John是一名打字员，他有一个习惯就是切换大小写时从来不按SHIFT键，而是只用Caps Lock键。老板为了监督John的工作，想统计John每天敲了多少次键盘，让我们编写一个函数来实现这个想法吧。

备注：输入的是字符串，只包含大小写英文字母。键盘初始默认是小写状态。

示例：
输入：aa，返回2，因为敲了a, a。
输入：Aa，返回4，因为敲了Cpas Lock, A, Cpas Lock, a。

题目难度：简单
题目来源：codewars 6
"""


def typist(words: str) -> int:
    # 键盘初始默认是小写状态，Cpas Lock灯关闭
    Cpas_Lock = False
    # 计数器初始化为0
    count = 0
    # 遍历每个字母
    for s in words:
        # 获取单个字母的 ASCII码
        strCode = ord(s)
        # 判断字母是大写还是小写
        # 大写字母ASCII码范围：65~90
        # 小写字母ASCII码范围：97~122
        strStatu = "大写字母" if strCode < 97 else "小写字母"
        if Cpas_Lock == False and strStatu == "大写字母":
            # 如果 Cpas Lock灯熄灭的，且敲出的是大写字母
            # 那么必需按 Cpas Lock建，将键盘大写打开才能敲出来
            Cpas_Lock = True
            # 计数器 +1
            count += 1
        elif Cpas_Lock == True and strStatu == "小写字母" :
            # 如果 Cpas Lock灯亮着，且敲出的是小写字母
            # 那么必需按 Cpas Lock建，将键盘大写关闭才能敲出来
            Cpas_Lock = False
            # 计数器 +1
            count += 1
        # 敲出字母本身，计数器 +1
        count += 1
    # 返回计数器的值
    return count

assert typist("aA") == 3
assert typist("Aa") == 4
assert typist("AAAaaaBBBbbbABAB") == 21