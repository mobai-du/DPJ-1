#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

def outer():
    a = 1
    def inner():
        print(a)
    return inner
inn = outer()
inn()

# import urllib
from urllib.request import urlopen
def get_url():
    url ="http://www.xiaohuar.com/"
    def get():
        res = urlopen(url).read()
        print(res)
    return get
get_abc = get_url()
get_abc()
