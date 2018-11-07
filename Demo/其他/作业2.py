#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

#1
# def sum_func(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(sum_func(1,2,3,4))
#2
a = 10
b = 20
def test(a,b):
    print(a,b)
c = test(b,a)
print(c)
#3
a = 10
b =20
def test5(a,b):
    a =3
    b =5
    print(a,b)
c = test5(b,a)
print(c)