#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('lisa',99)
print(lisa.name,lisa.get_grade())