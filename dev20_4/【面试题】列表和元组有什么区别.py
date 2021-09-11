
# 1、表现形式不一样，列表用[]，元组用()
mylist = ['a', 'b', 'c']
mytuple = ('a', 'b', 'c')

# 2、列表可修改，元组不可修改，但是可以增加
mylist[2] = 'd'
print(mylist)
try:
    mytuple[2] = 'd'
    print(mytuple)
except:
    print("出错，元组的元素不可修改")

# 3、只有单个元素时，列表不需要加逗号，元组需要加逗号
mylist+=['e']
print(mylist)
mytuple+=('e',)
print(mytuple)

# 4、列表和元组占用内存空间不一样
print(mylist.__sizeof__())
print(mytuple.__sizeof__())

# 5、元组可以作为字典的key使用，列表不可以
mydict1 = {mytuple:123}
print(mydict1)
try:
    mydict2 = {mylist:456}
    print(mydict2)
except:
    print("出错，列表不能作为字典的key使用")

# 6、元组可以计算出hash值，列表不可以
print(hash(mytuple))
try:
    print(hash(mylist))
except:
    print("出错，列表不能计算hash值")