import sys,os
print(dir())
print(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from proj import proj_1

"""
这项代码主要表示如何调用另一个包的模块。
首先获取路径，其次

"""