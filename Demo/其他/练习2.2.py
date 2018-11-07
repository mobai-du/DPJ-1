#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Student(object):

    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return  self.__gender

    def set_gender(self,gender):
        if gender in ['male','female']:
            self.__gender = gender
        else:
            raise ValueError('bad value')
bart = Student('bart','male')
# print(bart.get_gender())
print(bart.set_gender('female'))



class Student1(object):

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self,gender):
        if gender in ['male','female']:
            self.__gender = gender
        else:
            print("参数错误")

b = Student1('bar','male')
print(b.set_gender('male'))
print(b.get_gender())