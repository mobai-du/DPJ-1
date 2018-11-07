#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

import re
import json

f = open("1.txt","r")
date = f.read()
# print(date)

# print(type(date))
i = date.split()
print(type(i))
print(i)

# def yidong():
#     # i = re.findall("....", date)
#     i= re.findall('\D+',date)
#     # i = re.findall("1(3[4-9]){8}",date)
#     # i = re.findall("^1(3[4-9]|5[012789]|8[78]){8}",date)
#     # i = re.findall("134[0-9]+",date)
#     # i_2 = re.findall("135[0-9]{8}", date)
#     # i_3 = re.findall("136[0-9]{8}", date)
#     # i_4 = re.search("137[0-9]{8}", date).group()
#
#     # i_5 = re.findall("138[0-9]{8}", date)
#     # i_6 = re.findall("139[0-9]{8}", date)
#     # i_7 = re.findall("147[0-9]{8}", date)
#     # i_8 = re.findall("150[0-9]{8}", date)
#     # i_9 = re.findall("151[0-9]{8}", date)
#     # i_10 = re.findall("152[0-9]{8}", date)
#     # i_11 = re.findall("157[0-9]{8}", date)
#     # i_12 = re.findall("158[0-9]{8}", date)
#     # i_13 = re.findall("159[0-9]{8}", date)
#     # i_14 = re.findall("172[0-9]{8}", date)
#     # i_15 = re.findall("178[0-9]{8}", date)
#     # i_16 = re.findall("182[0-9]{8}", date)
#     # i_17 = re.findall("183[0-9]{8}", date)
#     # i_18 = re.findall("184[0-9]{8}", date)
#     # i_19 = re.findall("187[0-9]{8}", date)
#     # i_20 = re.findall("188[0-9]{8}", date)
#     # i_21 = re.findall("198[0-9]{8}", date)
#     # i= [i_1+i_2+i_3+i_4+i_5+i_6+i_7+i_8+i_9+i_10+i_11+i_12+i_13+i_14+i_15+i_16+i_17+i_18+i_19+i_20+i_21]
#     # print(i_4)
#
#     print(type(i))
#     print(i)
# yidong()
