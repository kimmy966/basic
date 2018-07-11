# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:09:21 2018

@author: WangNing
"""
'''
包含内容：
迭代器，生成器，装饰器，高级类
'''
##########迭代器##########
'''
除了内置的数据类型（列表、元组、字符串、字典等）可以通过 for 语句进行迭代，我们也可以自己创建一个容器，包含一系列元素，
可以通过 for 语句依次循环取出每一个元素，这种容器就是迭代器（iterator）。
除了用 for 遍历，迭代器还可以通过 next() 方法逐一读取下一个元素。要创建一个迭代器有3种方法，其中前两种分别是：
为容器对象添加 __iter__() 和 __next__() 方法（Python 2.7 中是 next()）；__iter__() 返回迭代器对象本身 self，
__next__() 则返回每次调用 next() 或迭代时的元素；
内置函数 iter() 将可迭代对象转化为迭代器
'''
# iter(IterableObject)
ita = iter([1, 2, 3])
print(type(ita))
 
print(next(ita))
print(next(ita))
print(next(ita))
 
# Create iterator Object
class Container:
    def __init__(self, start = 0, end = 0):
        self.start = start
        self.end = end
    def __iter__(self):
        print("[LOG] I made this iterator!")
        return self
    def __next__(self):
        print("[LOG] Calling __next__ method!")
        if self.start < self.end:
            i = self.start
            self.start += 1
            return i
        else:
            raise StopIteration()
c = Container(0, 5)
for i in c:
    print(i)
    
##########生成器##########
'''
前面说到创建迭代器有3种方法，其中第三种就是生成器（generator）。
生成器通过 yield 语句快速生成迭代器，省略了复杂的 __iter__() & __next__() 方式：
'''
def container(start, end):
    while start < end:
        yield start
        start += 1
c = container(0, 5)
print(type(c))
print(next(c))
next(c)
for i in c:
    print(i)

def gen():
    yield 5
    yield "Hello"
    yield "World"
    yield 4
for i in gen():
    print(i)
    
##生成器实现斐波那契数列
def fibonacci():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b
        
fib=fibonacci()
next(fib)
[next(fib) for i in range(10)]

def psychologist():
     print('Please tell me your problems')
     while True:
         answer = (yield)
         if answer is not None:
             if answer.endswith('?'):
                 print ("Don't ask yourself " 
                        "too much questions")
             elif 'good' in answer:
                 print ("That's good, go on")
             elif 'bad' in answer:
                 print ("Don't be so negative")
 
free = psychologist()
next(free)
free.send('I feel bad')
free.send("Why I shouldn't ?")
free.send("ok then i should find what is good for me")

def my_generator():
     try:
         yield 'something' 
     except ValueError:
         yield 'dealing with the exception'
     finally:
         print ("ok let's clean")
 
gen = my_generator()
next(gen)
gen.throw(ValueError('mean mean mean'))
gen.close()
next(gen)


from itertools import groupby
def compress(data):
    return ((len(list(group)), name)
            for name, group in groupby(data))

def decompress(data):
    return (car * size for size, car in data)

list(compress('get uuuuuuuuuuuuuuuuuup'))

compressed = compress('get uuuuuuuuuuuuuuuuuup')
''.join(decompress(compressed))

3*'a'+2*'b'

##########装饰器,内嵌函数###########



def outer():
    x = 1
    def inner():
        print(x) # 1
    inner() # 2
outer()

def logger(func):
    def inner(*args, **kwargs): #装饰器具有通用性，为适应不同函数的不同参数输入所以使用无限参数
        print( "Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) #2
    return inner
    
@logger
def foo1(x, y=1):
    return x * y
@logger
def foo2():
    return 2
foo1(5, 4)

foo1(1)

foo2()

def foo(*args, **kwargs):
    print ('args = ', args)
    print ('kwargs = ', kwargs)
    print ('---------------------------------------')

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)
#输出结果如下：
args =  (1, 2, 3, 4) 
kwargs =  {} 
#--------------------------------------- 
args =  () 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
#--------------------------------------- 
args =  (1, 2, 3, 4) 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
#--------------------------------------- 
args =  ('a', 1, None) 
kwargs =  {'a': 1, 'c': 3, 'b': '2'} 
#---------------------------------------

#可以看到，这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；
#**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，
#像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。

###########高级类##########
'''
面向对象编程：类
封装性，多态性，继承性
'''


class Student():           
    #class
    number=0                     #类变量
    def __init__(self,name,age): #实例方法
        self.name=name           #实例变量
        self.age=age
        self.__score=0           #私有化变量，外部无法直接访问，变成'_Student__score'
        self.__class__.number+=1
        print('当前学生人数：'+str(self.__class__.number))
    def marking(self,score):  #用方法去保护部分数据安全
        if score < 0:
            self.__score = 0
        self.__score=score
        print(self.name+' : '+str(self.__score))
    def __marking(self,score):  #用双下划线定义私有，无法从外部访问，前后都加则无效
        if score < 0:
            score = 0
        self.score=score
        print(self.name+' : '+str(score))
    def do_homework(self):
        self.do_english_homework()
        print(self.name+'is doing homework.')
    def do_english_homework(self):
        print(self.name+'is doing english homework.')
    @classmethod  # 类方法,直接操作类变量
    def plus_sum(cls):
        cls.number+=1
        print(cls.number)
    @staticmethod #静态方法，也可以访问类变量，不可以访问实例变量
    def add(x,y):
        print(Student.number)
        print('This is a static method.')

student1=Student('wangning',24) 
Student.plus_sum() 
student1.do_homework() 
student1.marking(99) 
print(student1.__dict__)
student1.__marking(99) 
student1.score
student1._Student__score  #强制读取私有变量
student2=Student('hanmeimei',23)
student2.plus_sum()  
student3=Student('lilei',22)  
student3.add(1,2)

#类的继承
class People():
    def __init__(self,name,age): #实例方法
        self.name=name           #实例变量
        self.age=age
    def get_name(self):
        print(self.name,self.age)
    def do_homework(self):
        print('Parent is doing homework.')
class Student1(People):           #继承父类,可以继承多个父类
    def __init__(self,school,name,age): #子类中调用父类的继承函数
        self.school=school         
        #People.__init__(self,name,age)  #!!!!self要传递!!!!  用类调用方法时候要有参数
        super(Student1,self).__init__(name,age) #调用父类不用输入父类名称
    def do_homework(self):
        super(Student1,self).do_homework()
        print(self.name+'is doing homework.')

student1=Student1('PKU','wangning',24)
student1.name
student1.get_name()
student1.do_homework()