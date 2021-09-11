
namelist = ['a', 'b', 'c']
print('my is name {}、{}、{} '.format(*namelist))

namedict = {'a':1, 'b':2, 'c':3}
print("my is name {a}、{b}、{c}".format(**namedict))

def func():
    return "我是函数"

name = "SMWHff"
print(f"my name: {name}  list： {namelist}  dict: {namedict}  func: {(lambda x:x+1)(2)}" )