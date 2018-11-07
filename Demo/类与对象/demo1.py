#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du
"""
面向对象编程就是对“类”跟“对象”的使用，类是一个模板，模板中可以包含多个函数，函数中实现一些功能
对象则是根据模板创建的实例，通过实例对象可以执行类中的函数

"""
class Foo:#类名

    def Bar(self):#self为特殊参数，必须填写
        print("abc")

    def Hello(self,name):
        print("i am %s" %name)
#根据类Foo创建对象obj，之后再引用
obj = Foo()
obj.Bar()
obj.Hello("abc")



#面向对象的三大特性:封装、继承、多态

"""
封装：就是将内容封装在某个地方，以后再去调用被封装在的某处的内容。
"""

class Foo1:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)
#根据类Foo1创建对象
#自动执行Foo1类的__init__方法
obj1 = Foo1("dupeng",18)#将dupeng和18分别封装到obj1  self 的name和age属性中

#根据类Foo1创建对象
#自动执行Foo1类的__init__方法
obj2 = Foo1("alex",73)#将alex和73分别封装到obj2   self 的name和age属性中
#self 是一个形式参数，当执行 obj1 = Foo('wupeiqi', 18 ) 时，self 等于 obj1
#当执行 obj2 = Foo('alex', 78 ) 时，self 等于 obj2


"""
调用：1,通过对象直接调用
2，通过self间接调用
"""
print(obj1.name)
print(obj1.age)

print(obj2.name)
print(obj2.age)


#间接调用
obj1.detail()
obj2.detail()

