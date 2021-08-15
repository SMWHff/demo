# 下面哪些代码有语法错误?
a = 1
b = 1
a, b = b, a
# a,b=1,2
# print(a) if a==b else print(b)
# a = 1
# if a = 1: print("aaa")

# 5. （单选）关于python的语法，下面的说法错误的是？
dic = {'a':123, 'b':456, 'c':789}
# print(dic[0])
# 字典是无序的

t = (1,2,3)
print(dir(tuple))

s = [1,2,3,4,5,6]
print(s[1:4:2])

list_a = [1,2,3]
list_a.extend([4,5])
list_a.append([4,5])
# list_a.add([4, 5])
print(list_a)
print(dir(list))
print(dir(dict))
print(dir(set))

{1}.