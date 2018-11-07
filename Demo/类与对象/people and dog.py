#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

def person(name,age,sex,job):
    def walk(p):
        print("person %s is walking..." % p['name'])
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }

    return data

def dog(name,dog_type):
    def bark(d):
        print("dog %s:wang.wang..wang..."%d['name'])
    data = {
        'name':name,
        'type':dog_type
    }
    return  data

# def bark(d):
#     print("dog %s:wang.wang..wang..."%d['name'])

# def walk(p):
#     print("person %s is walking..."%p['name'])

d1 = dog('lilei','jingba')

p1 = person('a',12,'F','运维')

p2 = person('b',123,'F','TE')

d1['bark'](p1)