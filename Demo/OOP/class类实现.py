#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Role(object):#定义一个类，class是定义类的语法，Role是类名，object是新式类的写法，必须这样写
    def __init__(self,name,role,weapon,life_value=100,money=15000):#初始化函数，在生成一个角色时要初始化一些属性就填写在这儿
        self.name = name#__init__中的第一个参数self，和这里的self都是什么意思？
        self.roel = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,i got shot")

    def buy_gun(self,gun_name):
        print("just bought %s "%gun_name)

r1 = Role('alex','police','ak47')
r2 = Role('jack','terrorist','b22')


