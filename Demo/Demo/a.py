#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

s  = 'ABCDEFG'
s1 = s[3::-2]
print(s1)
s2 = s[0:5:2]#[首，尾，步长] 切片：顾头不顾尾
print(s2)
s3 =s[4:0:-1]
print(s3)
s4 = s[3:0:-1]
print(s4)
s5 = s[4::-1]
print(s5)
s6 = s[::-1]
print(s6)
s7 = s[:]
print(s7)