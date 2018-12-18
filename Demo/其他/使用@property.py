#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Student(object):

    @property
    def get_score(self):
        return self.__score

    @score.setter
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError("score must between 0 ~100")
        self.__score = value

s = Student()
s.score =9999
# s.set_score(60)
# print(s.get_score())
# s.set_score(9999)
s.score = 60
print(s.score)