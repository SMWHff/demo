import tkinter as tk
import tkinter.messagebox as msg


def onclick(echo, value):
    """
    响应按钮事件
    """
    look = str(echo[0]['text'])
    num = echo[1]['text']
    if type(value) in (int, float):
        look = str(look) + str(value)
    elif value == '.':
        look = str(look) + str(value)
    elif value in ('+', '-', '*', '/', '%'):
        if look == "":
            look = num
        look = str(look) + str(value)
    elif value == '=':
        if look not in "=":
            look = eval(look)
            num = look
    elif value == 'CE':
        if len(look) > 0:
            while look[-1].isdigit() or look[-1] == '.':
                look = look[:-1]
                if len(look) == 0:
                    break
        num = 0
    elif value == 'C':
        look = ''
        num = 0
    elif value == '←':
        if len(look) > 0:
            look = look[:-1]
    else:
        msg.showinfo(f"崩溃！出错异常：{str(value)}")
    echo[0]['text'] = look
    echo[1]['text'] = str(num)[:14]
    return num


# 实例化TK
win = tk.Tk()
# 设置窗口标题
win.title("简易计算器")
# 设置窗口大小，并指定位置
win.geometry("320x503+900+100")
# 设置窗口宽度和高度不可改变
win.resizable(width=False, height=False)


# 显示计算过程控件
screen = [None, None]
screen[0] = tk.Label(text='', font=('微软雅黑', 10), foreground="#6F6C69", anchor='se')
screen[0].place(x=0, y=0, width=320, height=50)
# 显示计算结果控件
screen[1] = tk.Label(text='0', font=('微软雅黑', 30), anchor='se')
screen[1].place(x=0, y=55, width=320, height=50)


# 控件上的功能列表
list_text = ['%', 'CE', 'C', '←']
list_text += [7, 8, 9, '/']
list_text += [4, 5, 6, '*']
list_text += [1, 2, 3, '-']
list_text += [0, '.', '=', '+']

# 绘制按钮控件
for h in range(5):
    for l in range(4):
        index = h*4+l
        val = list_text[index]
        if type(val) == int:
            bg = "#FFFFFF"
        elif val == '=':
            bg = "#2185d0"
        elif val in ('+', '-', '*', '/'):
            bg = '#f2711c'
        else:
            bg = None
        btn = tk.Button(win, text=list_text[index], font=('微软雅黑', 16), background=bg)
        btn['command'] = lambda control=screen, value=val: onclick(control, value)
        btn.place(x=l*80, y=103+h*80, width=80, height=80)

# 显示主界面
win.mainloop()












# global_calc = []
# def onclick(echo, value):
#     """
#     响应登录事件
#     """
#     global global_calc
#     num = echo[1]['text']
#     print("value=", value, type(value))
#     if type(value) in (int, float):
#         if len(global_calc) == 0:
#             num = value
#             global_calc = [num]
#         else:
#             calc = global_calc[-1]
#             if type(calc) in (int, float):
#                 num = eval(f"{calc}{value}")
#                 global_calc[-1] = num
#             else:
#                 num = value
#                 global_calc.append(num)
#     elif value == '.':
#         if len(global_calc) == 0:
#             num = "0."
#             global_calc = [num]
#         else:
#             calc = global_calc[-1]
#             if calc[-1] == ".":
#                 num = calc
#                 global_calc[-1] = num
#             elif type(calc) in (int, float):
#                 num = f"{calc}{value}"
#                 if num[-1] != ".":
#                     num = float(num)
#                 global_calc[-1] = num
#             else:
#                 num = value
#                 global_calc.append(num)
#     elif value in ('+', '-', '*', '/', '%'):
#         if len(global_calc) == 0:
#             num = 0
#             global_calc = [num, value]
#         else:
#             calc = global_calc[-1]
#             if calc in ('+', '-', '*', '/', '%'):
#                 global_calc[-1] = value
#             else:
#                 if len(global_calc) > 1:
#                     list_temp = [str(v) for v in global_calc]
#                     num = eval(''.join(list_temp))
#                 global_calc = [num, value]
#     elif value == '=':
#         if len(global_calc) == 0:
#             global_calc = [num]
#         calc = global_calc[-1]
#         if calc == '=':
#             global_calc[-1] = value
#         else:
#             list_temp = [str(v) for v in global_calc]
#             num = eval(''.join(list_temp))
#             echo[0]['text'] = "".join(list_temp) + "="
#             global_calc = []
#     elif value == 'C':
#         global_calc = []
#         num = 0
#     elif value == '←':
#         num = num[:-1]
#     else:
#         msg.showinfo(f"崩溃！出错异常（{value}）")
#     echo[1]['text'] = str(num)[:14]
#     if len(global_calc) > 0:
#         list_temp = [str(v) for v in global_calc]
#         echo[0]['text'] = "".join(list_temp)
#     print(global_calc, num)
#     return num