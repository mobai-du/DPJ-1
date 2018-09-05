#coding:utf-8
# data = {
#
#     'roles':[
#         {'role':'monster','type':'pig'},
#         {'role':'hero','type':'关羽'},
#     ]
#
# }

#保存数据
# f  = open("game_status",'w',encoding='utf-8')
# f.write(str(data))

#提取数据
f = open("game_status",'r',encoding='utf-8')
d = f.read()
# print(d['roles'])
d = eval(d)
print(d['roles'])

'''
吧内存数据转成字符串叫序列化
吧字符串转成内存数据叫反序列化
'''