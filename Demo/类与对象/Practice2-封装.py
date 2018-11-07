#!/usr/bin/env python
#$ coding:utf-8 $
#__Author__:Peter Du

class person:

    def __init__(self,name,gender,age,npc):
        self.name = name
        self.gender = gender
        self.age = age
        self.npc = npc
    # def cang(self):
    #     print("%s,%s,%s,初始战斗力$s")%(self.name,self.gender,self.age,self.npc)
    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""
        self.npc = self.npc - 200

    def practice(self):
        """注释：自我修炼，增长100"""
        self.npc = self.npc + 200

    def incest(self):
        """注释：多人游戏，消耗500"""
        self.npc = self.npc - 500

    def detail(self):
        """注释：当前对象的详细情况"""
        temp ="姓名：%s;性别：%s;年龄：%s;战斗力：%s"%(self.name,self.gender,self.age,self.npc)
        print(temp)




########################开始游戏##############################


cang = person("藏静静","女",18,1000)
dong = person("懂你木木","女",20,1800)
bo = person("博多多","女",19,2500)

cang.incest()
dong.practice()
bo.grassland()

cang.detail()
dong.detail()
bo.detail()

cang.incest()
dong.practice()
bo.grassland()

cang.detail()
dong.detail()
bo.detail()