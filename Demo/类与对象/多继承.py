#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

# 1、Python的类可以继承多个类，Java和C#中则只能继承一个类

# 2、Python的类如果继承了多个类，那么其寻找方法的方式有两种，分别是：深度优先和广度优先

# 当类是经典类时，多继承情况下，会按照深度优先方式查找
"""
查找顺序：C->A->X->B
深度优先，是先找第一个查到底(object)
"""
# 当类是新式类时，多继承情况下，会按照广度优先方式查找
"""
查找顺序：C->A->B->X
广度优先，是先查找第一个，下一个将要查到底的时候，重新查下一个参数。
"""

class X(object):
    def f(self):
        print('x')

class A(X):
    def f(self):
        print('a')

    def extral(self):
        print('extral a')

class B(X):
    def f(self):
        print ('b')

    def extral(self):
        print('extral b')

class C(A, B, X):
    def f(self):
        super(C, self).f()
        print ('c')

print (C.mro())

c = C()
c.f()
c.extral()