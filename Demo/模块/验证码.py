#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

import random
a = random.randint(1,3)
b = random.sample("asdasgfiu132",3)#返回多个随机值
c = random.choice("asdhuhurh14211")#返回一个随机的字符串
print(a,b,c)
#生成随机字符串
import string
s = string.ascii_lowercase + string.digits + string.ascii_uppercase
#小写字母+
d = "".join(random.sample(s,6))
print(d)