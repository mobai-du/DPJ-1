#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Studnet(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Studnet.count += 1

a = Studnet('abc')
print(Studnet.count)
b = Studnet('def')
print(Studnet.count)
