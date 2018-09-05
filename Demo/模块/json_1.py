import  json
# data = {
#
#     'roles':[
#         {'role':'monster','type':'pig'},
#         {'role':'hero','type':'关羽'},
#     ]
# }
#dumps
# d = json.dumps(data)
# print(d,type(d))

#dump
# f = open("test.json","w")
# d = json.dump(data,f)

#loads
# d = json.dumps(data)#仅转成字符串
#
# d2 = json.loads(d)
# print(d2['roles'])

#load
# f = open("test.json",'r')
# data = json.load(f)
# print(data['roles'])

#-------------------------------
# f = open("json_file","w",encoding="utf-8")
#
# d = {'name':'alex','age':22}
# l = [1,2,3,4,'rain']
#
# json.dump(d,f)
# json.dump(l,f)


# f = open("json_file","r")
# b = json.load(f)
# print(b)
'''
注意json 中可以dump多次，但是load不可以提取出来
序列化：一次存，一次取
'''