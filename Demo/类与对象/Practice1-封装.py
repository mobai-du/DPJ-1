#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Foo:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def kanchai(self):
        print("%s,%s,%s,上山去砍柴"%(self.name,self.age,self.gender))


    def dongbei(self):
        print("%s,%s,%s,开车去东北" %(self.name, self.age, self.gender))


    def dabaojian(self):
        print("%s,%s,%s,最爱大宝剑" %(self.name, self.age, self.gender))


xiaomming = Foo("小明",10,"男")
xiaomming.kanchai()
xiaomming.dongbei()
xiaomming.dabaojian()

laoli = Foo("老李",90,"男")
laoli.kanchai()
laoli.dongbei()
laoli.dabaojian()