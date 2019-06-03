"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def myfilter(mystr):
    return len(mystr) == 6


# help()
print(chr(0x8d99))
print(hex(ord('趙')))
print(abs(-1.2345))
print(round(1.5678,2))
print(pow(1.2,1))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(0,4,2)])
print(fruits[0:4:2])
print(list(filter(myfilter,fruits)))
print(list(filter(None,fruits)))
print(filter(myfilter,fruits))

print(divmod(10,3))
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
tuple1=(1,2,3,4)
print(min(list2,list1))
print(min(list2))
print(max(list2,list1))
print(max(list2))
print(sum(list2))
print(sum(tuple1,3))
print(bin(3))