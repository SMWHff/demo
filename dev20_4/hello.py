#
#
# list_square = []
# for i in range(1,4):
#     list_square.append(i**2)
#
# print(list_square)
#
#
# list_square2=[i**2 for i in range(1,4)]
# # for i in range(1,4):
# #     list_square2.append(i**2)
# print("list_square2：", list_square2)
#
# list_square3=[i**2 for i in range(1,4) if i != 1 ]
# # for i in range(1,4):
# #     if i !=1:
# #         list_square3.append(i**2)
# print("list_square3：", list_square3)
#
#
# list_square4=[i*j for i in range(1,4) for j in range(1,4) ]
# # for i in range(1,4):
# #     for j in range(1,4):
# #         list_square4.append(i*j)
# print("list_square4：", list_square4)



a = {1, 2, 3}
b = {1, 4, 5}

print("并集：", a.union(b))
print("交集：", a.intersection(b))
print("差集：", a.difference(b))

# 字符串去重集合
set1 = set("sfahsgadhdgnadvgg")
set2 = {i for i in "sfahsgadhdgnadvgg" }
print("字符串去重集合1：", set1)
print("字符串去重集合2：", set2)


dict1 = {'a':1, 'b':2, 'c':3}
dict2 = dict(a=1, b=2)
print(dict1.popitem())
print(dict1)
a={}
b=a.fromkeys(['aa', 'bb', 'cc'], 123)
print(b)

c = {i:i*2  for i in range(1,4) }
print(c['temp_dict'])

