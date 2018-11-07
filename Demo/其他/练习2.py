#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du
'''
如果要让内部属性不被访问，可以吧属性的名称前加上两个下划线__，在python中，实例的变量名如果以__开头，
就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
'''
class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s"%(self.__name,self.__score))

    '''
    如果外部代码要获取name跟score？可以给student类增加get_name和get_score这样的方法

    '''
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    '''
    如果又要允许外部代码修改score？可以给student增加set_score方法
    '''
    # def set_score(self,score):
    #     self.__score = score
    #
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student("bart",59)
print(bart.__name)
print(bart.get_name(),bart.get_score())




