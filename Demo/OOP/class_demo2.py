#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Dog(object):

    def __init__(self,name,dog_type):
        self.name = name
        self.type = dog_type

    def sayhi(self):

        print("hello, i am a dog ,my name is ",self.name)

# d = Dog('LIchuang',"京巴")
# d.sayhi()
print(Dog)