#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du


class Hero:

    def __init__(self,nickname,aggressivity,life_value):#绰号，攻击性，生命值
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def move_forward(self):#向前移动
        print("%s move forward" %(self.nickname))

    def move_backward(self):
        print("%s move backward"%self.nickname)

    def move_left(self):
        print("%s move left" %self.nickname)

    def move_right(self):
        print("%s move right" %self.nickname)

    def attack(self,enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    pass


class Riven(Hero):
    camp = "Noxus"
    def attack(self,enemy):#在这儿定义新的attack，不再使用父类的attack，且不会影响父类
        print("from riven")


g1 = Garen("草丛伦",100,300)
r1 = Riven("瑞文",57,200)


print(g1.life_value)
r1.attack(g1)
print(g1.life_value)



class Foo:

    def f1(self):
        print("Foo.f1")

    def f2(self):
        print("Foo.f2")
        self.f1()

class Bar(Foo):

    def f1(self):
        print("Foo.f1")


b = Bar()
b.f2()

"""
打印结果
Foo.f2
Foo.f1
"""