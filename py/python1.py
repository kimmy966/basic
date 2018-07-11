# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:40:07 2017

@author: WangNing
"""
'''
包含内容：
输出，迭代，numpy相关，切片，copy，plot
'''
#无穷大与无穷小
float('inf')
float('-inf')>0.0001

a = input('please input your name :')

num1=3.14
type(num1)
repr(num1) #转化成字符串但不保存输出
type(num1)

# 输出字典中特定字段
dic={'a':1,'b':10}
print('a is %(a)f' % dic)

# 同时输出索引及内容
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx , animal))
    
## enumerate还可以接收第二个参数，用于指定索引起始值
for idx, animal in enumerate(animals,1):
    print('#%d: %s' % (idx , animal))

## list comprehension    
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares) 

## List comprehensions can also contain conditions
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

## loop dictionary
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
    
## Dictionary comprehensions
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)
    
## class
class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"

import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"
b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"
c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"
d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"
e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"
## 关于切片
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
c = a[0,0]
c=0
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
## 更改b中的值会改变a中的值
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1]) 

m = list(range(100))

m[:10]#取前十个数

m[-10:]#取后十个数

m[10:20]#取前11-20个数

m[:10:2]#前十个数中，每2个数取一个

m[5:15:3]#第6-15个数中，每3个数取一个

m[15:5:-1]#第6-15个数中，从第15倒取

m[::10]#所有的数中，每10个数取一个

m[:]#什么都不写，可以原样复制一个list


a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
          #                [ 4,  5,  6],
          #                [ 7,  8,  9],
          #                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])
# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
          #                [ 4,  5, 16],
          #                [17,  8,  9],
          #                [10, 21, 12]])
          
         
## Boolean array indexing         
a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2.

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])  

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
print(np.dot(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"


##sort
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),('alain','A',10)] 
sort= sorted(students, key=lambda kv: (-kv[2], kv[0]))

[i for i,a in enumerate(m) if a==[1,2,3]]

import numpy as np
a=[[1,2,3],
   [4,5,6]]
print("列表a如下：")
print(a)

print("增加一维，新维度的下标为0")
c=np.stack(a,axis=0)
print(c)

print("增加一维，新维度的下标为1")
c=np.stack(a,axis=1)
print(c)



a=[[1,2,3],
   [4,5,6]]
b=[[1,2,3],
   [4,5,6]]
c=[[1,2,3],
   [4,5,6]]
print("a=",a)
print("b=",b)
print("c=",c)

print("增加一维，新维度的下标为0")
d=np.stack((a,b,c),axis=0)
print(d)

print("增加一维，新维度的下标为1")
d=np.stack((a,b,c),axis=1)
print(d)
print("增加一维，新维度的下标为2")
d=np.stack((a,b,c),axis=2)
print(d)

a=[[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]],[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]]

c=np.stack(a,axis=0)
print(c)
c=np.stack(a,axis=1)
print(c)
c=np.stack(a,axis=2)
print(c)
c=np.stack(a,axis=3)
print(c)

## numpy.ravel() vs numpy.flatten()

x = np.array([[1, 2], [3, 4]])
x.flatten()[1] = 100   # flatten：返回的是拷贝
x
x=np.array([[1, 2],
       [3, 4]])            
x.ravel()[1] = 100
x


a = [1, 2, 3]

b = a

print (b)

a[0] = 0

print (b)

#解释：[1, 2, 3]被视作一个对象，a，b均为这个对象的引用，因此，改变a[0],b也随之改变

#如果希望b不改变，可以用到切片

b = a[:]

a[0] = 0

print (b)



#解释，切片a[:]会产生一个新的对象，占用一块新的内存，b指向这个新的内存区域，因此改变a所指向的对象的值，不会影响b



#浅拷贝

import copy

a = [1, 2, 3, [5, 6]]

b = copy.copy(a)

print (b)


a[3].append('c')

print (b)


#深拷贝

a = [1, 2, 3, [5, 6]]

b = copy.deepcopy(a)

a[3].append('c')

print (b)



#拷贝即是开辟一块新的内存空间，把被拷贝对象中的值复制过去。而浅拷贝并没有为子对象[5,6]开辟一块新的内存空间，而仅仅是实现对a中[5，6]的引用。所以改变a中[5，6]的值，b中的值也会发生变化。
#深拷贝则是为子对象也开辟了一块新空间。所以改变a中[5, 6]的值，并不影响b

 

#数组赋值不能用切片来达到相同的目的

import numpy as np

a = np.array([1, 2 ,3])

b = a[:]

a[0] = 5

print( a, b)



#如上，虽然用切片，但不能达到修改a而不影响b的目的。说明a,b仍然指向同一块内存。


b = a.copy()

a[0] = 5

print( a, b)


#注意，列表的拷贝是copy.copy(obj)或copy.deepcopy(obj),数组的拷贝是obj.copy()


A={'a':2,'b':4}
A.pop('c',10)
A.pop('a',10)

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2
y3 = x
y4 = x**3 +1 

plt.figure()
# 在绘制时设置lable, 逗号是必须的
l1, = plt.plot(x, y1, color = 'royalblue', linewidth = 2.0)
l2, = plt.plot(x, y2,  color = 'deepskyblue', linewidth = 2.0)
l3, = plt.plot(x, y3,  color = 'tomato', linewidth = .5, linestyle = '-', marker='*')
l4, = plt.plot(x, y4,  color = 'salmon', linewidth = .5, linestyle = '-', marker='*')
plt.legend(handles = [l1, l2, l3, l4,], labels = ['a', 'b','c','d'], loc = 'best')
plt.show()