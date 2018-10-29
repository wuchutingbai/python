# #可调用对象
# def foo():
#     print('hello')
# foo()#这个和下面的意思是一样的
# foo.__call__()
#
# #__call__类中的第一个方法，实例就可以向函数一样调用
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __call__(self,*args,**kwargs):
#         return 'Point({},{})'.format(self.x,self.y)
#
# p = Point(4,5)
# print(p.__dict__)
# print(p())
#
# class Adder:
#     def __call__(self,*args):
#         ret = 0
#         for x in  args:
#             ret += x
#         self.ret = ret
#         return ret
#
# adder = Adder()
# print(adder(2,3,4,5,8))
# print(adder.ret)
#
# #定义一个斐波那契数列，方便调用。计算第n项目
# class Fib:
#     def __init__(self):
#         self.items = [0,1,1]
#     def __call__(self,index):
#         return self[index]
#     def __iter__(self):
#         return iter(self.items)
#     def __len__(self):
#         return len(self.items)
#     def __getitem__(self,index):
#         if index < 0:
#             raise IndexError('Wrong Index')
#         if index < len(self.items):
#             return self.items[index]
#         for i in range(3,index+1):
#             itm = self.items[i-1] + self.items[i-2]
#             if itm  not in self.items:
#                 self.items.append(self.items[i-1] + self.items[i-2])
#         return self.items[index]
#     def __str__(self):
#         return str(self.items)
#     __repr__ = __str__
# fib = Fib()
# print(fib(5),len(fib))
# print(fib(10),len(fib))
# for x in fib:
#     print(x)

# #上下文管理
# import sys
# class Point:
#     def __init__(self):
#         print('init')
#     def __enter__(self):
#         print('enter')
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print('异常类型',exc_type)
#         print('异常的值',exc_val)
#         print('异常信息追踪',exc_tb)
#         print('exit')
#
# with Point() as f:
#     raise Exception('New error')
#     print('do sth')
#     print(f)

#练习 位加法函数计时

# #运用装饰器
# import datetime
# import time
# from functools import wraps
#
# def  timeit(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args,**kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print('{} took {}s'.format(fn.__name__,delta))
#         return ret
#     return  wrapper
# @timeit
# def add(x,y):
#     time.sleep(2)
#     return x + y
# print(add(4,5))

#运用上下文管理
# import time
# import datetime
# from functools import wraps
#
# def add(x,y):
#     time.sleep(2)
#     return  x + y
#
#
# class TimeIt:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         self.delta = (datetime.datetime.now() -  self.start).total_seconds()
#         print('{} took {}s'.format(self.fn.__name__,self.delta))
#         pass
#     def __call__(self,x,y):
#         print(x,y)
#         return self.fn(x,y)
#
# with TimeIt(add) as foo:
#     foo(4,6)


# #运用类装饰器来实现
# import time
# import datetime
# from  functools import wraps
#
# class TimeIt:
#     '''this is a class'''
#     def __init__(self,fn = None):
#         if fn is not None:
#             self.fn = fn
#         #self.__doc__ = fn.__doc__
#         wraps(fn)(self)
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print('{} took {}s'.format(self.fn.__name__,self.delta))
#     def __call__(self,*args,**kwargs):
#         return self.fn(*args,**kwargs)
# @TimeIt
# def add(x,y):
#     '''this is a add function'''
#     return x + y
#
# print(add(4,5))
# print(add.__doc__)
# print(TimeIt.__doc__)


# #反射
# class Point:
#     def __init__(self,x,y,z=None):
#         self.x = x
#         self.y = y
#     def __str__(self):
#          return 'Point({},{})'.format(self.x,self.y)
#     def show(self):
#         print(self.x,self.y)
#
# p1 = Point(4,5)
# p2 = Point(10,10)
# print(p1,p2)
# print(repr(p1),repr(p2),sep = '\n')
# print(p1.__dict__)
# setattr(p1,'y',20)
# setattr(p1,'z',9)
# print(getattr(p1,'__dict__'))
#
# if hasattr(p1,"show"):
#     getattr(p1,'show')()
# if not hasattr(p1,'add'):
#     setattr(Point,'__add__',lambda self,other:Point(self.x + other.x,self.y + other.y))
# print(Point.__add__)
# print(p2+p1)
# if not hasattr(p1,'sub'):
#     setattr(p1,'sub',lambda self,other:Point(self.x - other.x,self.y - other.y))
# print(p1.sub(p1,p1))
#
# print(p1.__dict__)
# print(Point.__dict__)


# #用类来实现命令分发器
# class Dispatcher:
#     def __init__(self):
#         self._run()
#     def cmd1(self):
#         print("i'm cmd1")
#
#     def cmd2(self):
#         print("i'm cmd2")
#
#     def _run(self):
#         while True:
#             cmd = input('Plz input a cmd')
#             if cmd.strip() == 'quit':
#                 break
#             getattr(self,cmd,lambda:print('Unknown Command{}'.format(cmd)))
#         Dispatcher()

#反射相关的魔术方法
# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)
#     def __getattr__(self, item):
#         return 'missing {}'.format(item)
#
# p1 = Point(4,5)
# print(p1.x)
# print(p1.z)
# print(p1.n)
# print(p1.t)#missing t


# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self,x,y):
#         print('init')
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)
#     def __getattr__(self, item):
#         return 'missing {}'.format(item)
#     def __setattr__(self,key,value):
#         print('setattr {} = {}'.format(key,value))
#
# p1 = Point(4,5)
# p1.t = 100
# print('1',p1.x)
# print('2',p1.y)
# print('3',p1.z)
# print('4',p1.n)
# print('5',p1.t)#missing t


# class Base:
#     n = 0
#
# class Point(Base):
#     z = 6
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)
#     def __getattr__(self, item):
#         return 'missing {}'.format(item)
#     def __getattribute__(self, item):
#         return item
#
# p1 = Point(4,5)
# print(p1.__dict__)
# print(p1.x)
# print(p1.z)
# print(p1.n)
# print(p1.t)#missing t
# print(Point.__dict__)
# print(Point.z)


#描述器
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#
# print('-'*20)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x.a1)


#加入__get__函数
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self,instance,owner):
#         print('A.__get__{} {} {}'.format(self,instance,owner))
#         return self #解决返回值是None的问题
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#
# print('-'*20)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x.a1)

#类B的实例属性可以吗
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self,instance,owner):
#         print('A.__get__{} {} {}'.format(self,instance,owner))
#         return self #解决返回值是None的问题
#
# class B:
#     x = A()
#     def __init__(self):
#         self.b = A()
#         print('B.init')
#
# print('-'*20)
# print(B.x)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x)
# print(b.x.a1)
#print(b.b)#访问实例的属性并不会触发get函数


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self,instance,owner):
#         print('A.__get__{} {} {}'.format(self,instance,owner))
#         return self #解决返回值是None的问题
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#         self.x = 'b.x'#增加实例属性
#
# print('-'*20)
# print(B.x)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x)
# #print(b.x.a1)


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self,instance,owner):
#         print('A.__get__{} {} {}'.format(self,instance,owner))
#         return self #解决返回值是None的问题
#
#     def __set__(self,instance,value):
#         print('A.__set__ {} {} {}'.format(self,instance,value))
#         self.data = value
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#         self.x = 'b.x'
#
# print('-'*20)
# print(B.x)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x)
# print(b.x.a1)
# print(A.__dict__)
# print(B.__dict__)
# print(b.__dict__)
# b.x = 500
# print(A.__dict__)
# print(B.__dict__)
# print(b.__dict__)
# B.x =600
# print(A.__dict__)
# print(B.__dict__)
# print(b.__dict__)



#描述其的本质
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self,instance,owner):
#         print('A.__get__{} {} {}'.format(self,instance,owner))
#         return self #解决返回值是None的问题
#
#     def __set__(self,instance,value):
#         print('A.__set__ {} {} {}'.format(self,instance,value))
#         self.data = value
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#         self.x = 'b.x'
#         self.y = 'b.y'
#
# print('-'*20)
# print(B.x)
# print(B.x.a1)
#
# print('='*20)
# b = B()
# print(b.x)
# print(b.y)
# print(b.__dict__)
# print(B.__dict__)
