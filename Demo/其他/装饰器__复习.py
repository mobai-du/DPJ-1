#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

'''
装饰器:用于拓展原来函数功能的一种函数，特点在于它的返回值也是一个函数，
好处是在不改变源码的前提下，给函数增添新的功能
'''
import  time
def func():
    print('hello')
    time.sleep(1)
    print('world')
func()