# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:06:30 2017

@author: WangNing
"""
'''
包含内容：
路径获取，文件读取，二进制转化，内存管理，正则表达式与json,枚举
函数式编程：闭包，匿名函数lambda
zip()
'''
from os import walk
from os import path
def get_fileNames(rootdir):
    data=[]
    for root, dirs, files in walk(rootdir, topdown=True):
        for name in files:
            _, ending = path.splitext(name)
            if ending != ".jpg" and ending != ".jepg" and ending != ".png":
                continue
            else:
                data.append(path.join(root, name))
    return data


aa=open('aa.txt','r')

for haha in aa.readlines():
    print(haha)

for wahaha in aa.readlines():
    print(wahaha)
'''
 文件迭代象第其迭代候haha候aa.readlines()返aa.txt文件字符串列表(第元素aa.txt第行第二元素aa.txt第二行类推)指针已经aa.txt第行移行指针状态指向行所第二wahaha候aa.readlines()空列表空列表迭代都没啦
        解决第二迭代前aa指针复位第行添加aa.seek(0)行代码第二迭代前啦
'''

x = open('my.log', 'r')    #读取一个文件  
x.tell()           #获得当前文件读取指针  
#0L              #当前文件指针在文件头处  
x.seek(3)          #将文件指针向前移动3个字节  
x.tell()  
#3L            #指针已经移动到了第3个字节处  
x.seek(5,1)            #表示从文件头处开始移动指针，向前移动5个字节  
x.tell()                 
#5L             #当前文件读取指针已经移动到第5个字节处  
x.seek(0,0)            #表示将文件指针移动到文件头处  
x.tell()  
#0L
x.seek(0,2)            #表示将文件读取指针移动到文件尾部  
x.tell()                 
#214L                #可以得到文件大小为214B  
x.seek(-2,2)       #表示从文件尾部开始移动指针，向后移动2个字节  
x.tell() 



##二进制的转换
import struct
import binascii
values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)
 
print ('Original values:', values)
print ('Format string :', s.format)
print ('Uses :', s.size, 'bytes')
print ('Packed Value :', binascii.hexlify(packed_data))
print ('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)

import struct
import binascii
import ctypes
 
values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
prebuffer = ctypes.create_string_buffer(s.size)
print ('Before :',binascii.hexlify(prebuffer))
s.pack_into(prebuffer,0,*values)
print ('After pack:',binascii.hexlify(prebuffer))
unpacked = s.unpack_from(prebuffer,0)
print ('After unpack:',unpacked)

'''
对比使用pack方法打包，pack_into 方法一直是在对prebuffer对象进行操作，没有产生多余的内存浪费。
另外需要注意的一点是，pack_into和unpack_from方法均是对string buffer对象进行操作，并提供了offset参数，
用户可以通过指定相应的offset，使相应的处理变得更加灵活。例如，我们可以把多个对象pack到一个buffer里面，
然后通过指定不同的offset进行unpack：
'''
values1 = (1, 'abc', 2.7)
values2 = ('defg',101)
s1 = struct.Struct('I3sf')
s2 = struct.Struct('4sI')
 
prebuffer = ctypes.create_string_buffer(s1.size+s2.size)
print ('Before :',binascii.hexlify(prebuffer))
s1.pack_into(prebuffer,0,*values1)
s2.pack_into(prebuffer,s1.size,*values2)
print ('After pack:',binascii.hexlify(prebuffer))
print (s1.unpack_from(prebuffer,0))
print (s2.unpack_from(prebuffer,s1.size))

#python的内存管理
a = 1
print(id(a))
print(hex(id(a)))
#在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用。
#当我们创建多个等于1的引用时，实际上是让所有这些引用指向同一个对象。
a = 1
b = 1

print(id(a))
print(id(b))

# True
a = 1
b = 1
print(a is b)

# True
a = "good"
b = "good"
print(a is b)

# False
a = "very good morning"
b = "very good morning"
print(a is b)

# False
a = []
b = []
print(a is b)

#我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。
from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = a
print(getrefcount(b))

class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))

from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))
#某个对象的引用计数可能减少。比如，可以使用del关键字删除某个引用:
a = [1, 2, 3]
b = a
print(getrefcount(b))

del a
print(getrefcount(b))
#如果某个引用指向对象A，当这个引用被重新定向到某个其他对象B时，对象A的引用计数减少
a = [1, 2, 3]
b = a
print(getrefcount(b))

a = 1
print(getrefcount(b))

#返回(700, 10, 10)，后面的两个10是与分代回收相关的阈值，后面可以看到。700即是垃圾回收启动的阈值。
#可以通过gc中的set_threshold()方法重新设置。
import gc
print(gc.get_threshold())

#python中的下划线
#在解释器中：在这种情况下，“_”代表交互式解释器会话中上一条执行的语句的结果。
1+1
#print(_)
#作为一个名称：“_”作为临时性的名称使用。但是并不会在后面再次用到该名称。
n = 42 
for _ in range(n): 
    print('a')


############正则表达式与json##########
import re
a='C|Python|Java|C++|C#'    
'Python' in a
a.index('Python')
re.findall('Python',a)

b='c0python1\njava\t 3c++4c#__'  
re.findall('\d',b)      #找出全部数字
re.findall('\D',b)      #找出全部非数字
re.findall('\w',b)      #找出全部数字字母以及下划线
re.findall('\W',b)      #找出非单词字符
re.findall('\s',b)      #找出空白字符
re.findall('[a-z]{1,6}',b) #找出1-6长度的字符串
re.findall('[a-z]{1,6}?',b) #非贪婪模式匹配！找出1-6长度的字符串

c='abc, acc, adc, cdc, dea'
re.findall('a[bcd]c',c)  #找出a为首c为尾的字符串
re.findall('a[^d]c',c)  #找出不是adc的a为首c为尾的字符串
re.findall('a[a-z]c',c)  #找出a为首c为尾的字符串

d='pytho0python1pythonn2'
re.findall('python*',d)  # '*'代表前面字符可以出现0次或无限多次
re.findall('python+',d)  # '+'代表前面字符可以出现1次或无限多次
re.findall('python?',d)  # '+'代表前面字符可以出现0次或1次

##边界匹配
a='1001'
re.findall('^\d{1,6}$',a) #'^'从字符串开始匹配'$'从字符串结尾匹配

b='PythonPythonC#\nPythonPythonC#C#'
re.findall('(Python){2}',b) #小括号为组
re.findall('c#.{1}',b,re.I|re.S) #re.I忽略大小写，re.S配合'.'使用匹配后面的一个字符
re.sub('C#','Go',b,0)
re.sub('C#','Go',b,1)
b.replace('C#','Go')
##函数替换         
def covert(value):
    pass
re.sub('C#',covert,b)
def covert1(value):
    matched=value.group()
    return '!!'+matched+'!!'
re.sub('C#',covert1,b)
       
s='a52b65c2d786e34f1'
re.match('\d',s)  #match 从首字母开始匹配
re.search('\d',s) #search 搜索整个字符串

s='life is short,i use python,i love python'
r=re.search('life.*python',s)
print(r.group())

r=re.search('life(.*)python(.*)python',s)
print(r.group(0,1,2))
print(r.groups())

##json JavaScript Object Notation

import json
json_str='[{"name":"wangning","age":18,"flag":false},{"name":"wangning","age":18}]'
student=json.loads(json_str)
print(student)

json_str1=json.dumps(student)
  

###########枚举##########
from enum import Enum,IntEnum,unique    

class VIP(Enum): #枚举禁止使用重复标签,数值相等则后面无效
    yellow = 1
    orange=1
    green =2
    red =3
    black ='b'
VIP.orange  
for v in VIP:                     #不会输出重复值
    print(v)
for v in VIP.__members__.items(): #可以输出重复值 
    print(v)
VIP.black =6                      #枚举类型禁止更改   
VIP.green.value
VIP.green.name
VIP(1)

@unique
class VIP(IntEnum): #unique装饰后不能出现重复值，intenum后不能出现非数字值
    yellow = 1
    orange=1
    green =2
    red =3
    black =4
    
##########函数式编程##########   
##闭包
def factory():
    pos=0
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return pos
    return go
tourist=factory()
tourist(2)
tourist(5)

##匿名函数
def add(x,y):
    return x+y

f = lambda x,y:x+y
f(1,2)

##三元表达式
x,y=(2,1)
r = x if x >y else y

##map函数
def square(x):
    return x**2
list_x=[1,2,3,4,5,6,7,8]
result=map(square,list_x)
result=map(lambda x : x**2,list_x)
print(list(result))

list_y=[1,2,3,4,5]
result1=map(lambda x,y: x*y,list_x,list_y)
print(list(result1))

##reduce函数
from functools import reduce
list_y=[1,2,3,4,5]
reduce(lambda x,y:x+y,list_y,10)
test=['a','b','c','d','e']
reduce(lambda x,y:x+y,test,'o')

##filter函数
list_x=[1,0,1,0,1]

r=filter(lambda x:True if x==1 else False,list_x)
print(list(r))

############zip()##########
## zip()函数单个参数
print('=*'*10 + "zip()函数单个参数" + '=*'*10)
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
# 打印zip函数的返回类型
print("zip()函数的返回类型：\n", type(tuple1))
# 将zip对象转化为列表
print("zip对象转化为列表：\n", list(tuple1))


## zip()函数有2个参数
print('=*'*10 + "zip()函数有2个参数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
p = [[2, 2, 2],  [3, 3, 3]]
# 行与列相同
print("行与列相同:\n", list(zip(m, n)))
# 行与列不同
print("行与列不同:\n", list(zip(m, p)))


## zip()应用，也可以使用for循环+列表推导式实现
# 矩阵相加减、点乘
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# 矩阵点乘
print('=*'*10 + "矩阵点乘" + '=*'*10)
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# 矩阵相加,相减雷同
print('=*'*10 + "矩阵相加,相减" + '=*'*10)
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])



## *zip()函数
print('=*'*10 + "*zip()函数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print("*zip(m, n)返回:\n", *zip(m, n))
m2, n2 = zip(*zip(m, n))
print(m == list(m2) and n == list(n2))