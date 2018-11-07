#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

# class C:
#
#     def __init__(self):
#         self.name = "公有字段"
#         self.__foo = "私有字段"
#

class C:

    name = "公有静态字段"

    def func(self):
        print(C.name)

class D:

    def show(self):
        print(C.name)

C.name

obj = C()
obj.func()

obj_son = D()
obj_son.show()

print(D.__doc__)