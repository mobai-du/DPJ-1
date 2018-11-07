#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

d = {
    "0":"零",
    "1":"一",
    "2":"二",
    "3":"三",
    "4":"四",
    "5":"五",
    "6":"六",
    "7":"七",
    "8":"八",
    "9":"九"

}

while True:
    ID = input("please input you ID\n").strip()
    if  ID.isdigit():
        ID = int(ID)
        print(ID)
        a1 = str(ID)
        a2 = list(a1)
        # print(a2)
        b1 = a2[6:10]
        # print(b1)
        c = list(d.values())
        # print(c)

        for i in b1:
            if i in d:
                print(d[i],end="",)
    else:
        print("not int")

