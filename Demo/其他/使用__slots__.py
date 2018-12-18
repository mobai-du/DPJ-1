#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du
from types import MethodType
class Student(object):


    def set_age(self, age):
        self.age = age


    def set_score(self,score):
        self.score = score
'''
给实例绑定属性
'''
s = Student()
s.name = 'abc'
print(s.name)
'''
   给实例绑定方法
   '''
# s.set_age = MethodType()
s.set_age(25)
print(s.age)

Student.set_score = set_score