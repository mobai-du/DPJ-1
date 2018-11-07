#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Animal:

    def eat(self):
        print("%s 吃"%self.name)

    def drink(self):
        print("%s 喝"%self.name)

    def shit(self):
        print("%s 啦"%self.name)

    def pee(self):
        print("%s 撒"%self.name)

class Cat(Animal):

    def __init__(self,name):
        self.name = name
        self.breed = "猫"

    def cry(self):
        print("喵喵叫")

class Dog(Animal):

    def __init__(self,name):
        self.name = name
        self.breed = "狗"

    def cry(self):
        print("汪汪叫")

#####执行###########s
c1 = Cat("小白家的小黑猫")
c1.eat()

c2 = Cat("小黑的小白马")
c2.drink()

c3 = Dog("胖子家的小收购")
c3.eat()




