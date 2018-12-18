#!/usr/bin/env python
#$ coding:utf-8 $
#__Author__:Peter Du

# count = 0
# while count <=100:
#     print("loop",count)
#     count += 1
#
# print("----loop end----")


# count  = 0
# while count<= 100:
#     if count % 2 ==0:
#         print("loop",count)
#     count += 1
# print("----loop end----")

#第50次不打印，第60-80打印对应值的平方
# count = 0
# while count <= 100:
#     if count == 50:
#         pass
#     elif 60 <= count <= 80:
#         print("loop",count**2)
#     else:
#         print("loop",count)
#     count += 1
#
# print("----loop end----")


# count = 0
# while count <= 100:
#     print("loop",count)
#     if count == 5:
#         break
#     count += 1
#
# print("---out of while loop---")
# count = 0
# while count <= 100:
#     print("loop",count)
#     if count == 5:
#         continue
#     count += 1
#
# print("---out of while loop---")
# count = 0
# while count <= 100:
#     count += 1
#     if count > 5 and count <95:
#         continue
#     print("loop ",count)
# user = "seven"
# pwd = '123'
# while True:
#     usname = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if usname == user and passwd == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
# user = "seven"
# pwd = '123'
# count = 0
# while True:
#     usname = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if usname == user and passwd == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#     count += 1
#     while count == 3:
#         choose = input("还要继续登录吗？y|n")
#         if choose == 'y':
#             count = 0
#         elif choose == 'n':
#             exit()
#         else:
#             print("您输入有误，请从新输入")

#
# user = ['seven','alex']
# pwd = '123'
# count = 0
# while True:
#     usname = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if usname in user and passwd == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#     count += 1
#     while count == 3:
#         choose = input("您还要继续登录吗?y|n")
#         if choose =="y":
#             count =0
#         elif choose == 'n':
#             exit()
#         else:
#             print("输入有误，重新输入")
# i = 2
# sum = 0
# while i < 100:
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
#     i += 1
# print('sum:',sum)
#方法1
# count = 1
# while count < 101:
#     print(count)
#     count += 2

#方法2
# count = 0
# while count < 101:
#     if count % 2 == 1:
#         print(count)
#     count += 1

# count = 0
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count += 1
# count = 1
# sum = 0
# while count < 101:
#     sum += count
#     count += 1
# print(sum)

# username = "abc"
# password = '123'
# count = 0
# while True:
#     user = input("输入用户名：")
#     passwd = input("输入密码：")
#     if user == username and passwd == password:
#         print("登录成功！")
#         break
#     else:
#         print("登录失败，请重新输入！")
#     count += 1
#     if count == 3:
#         print("登录失败错误过多，程序将退出！")
#         break
# username = "abc"
# password = '123'
# count = 0
# while True:
#     user = input("输入用户名：")
#     passwd = input("输入密码：")
#     if user == username and passwd == password:
#         print("登录成功！")
#         break
#     else:
#         print("登录失败，请重新输入！")
#     count += 1
#     if count == 3:
#         print("登录失败错误过多，程序将退出！")
#         break
# user = 'abc'
# pwd = 123
# i = 0
# while i < 3 :
#     username = input("输入用户名：")
#     password = int(input("输入密码："))
#     if username == user and password == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#     i += 1
#
# import  os#导入包
# user_list = {
#     'alex':{'password':'123'},
#     'jack':{'password':'123'}
# }
# if os.path.exists('lock'):#判断文件是否存在，如存在，就读取，否则创建一个新文件。
#     f = open('lock', 'r',encoding =' utf-8')
# else:
#     f = open('lock','w')
# with open('lock','r') as f1:
#     lock_user = f1.read()
#
# count = 0
# while count < 3:
#     username = input("please input you username:")
#     if username == lock_user:#判断用户名是否锁定
#         print("username is lock!!!")
#     else:
#         if username not in user_list:
#             print("not find username!")
#         else:
#             password = input("please input your password:")
#             if password == user_list[username]['password']:#判断密码是否正确
#                 print("welcome %s"%username)
#                 break
#             else:
#                 print("password is error,please again")
#     count += 1
#     if count == 3:#账号锁定
#         with open('lock','a') as f2:#a'表示append，表示不清除原有数据，在原有数据之后，继续写数据
#             f2.write(username)
# else:
#     print("Three errors will be locked!")

# name1 = 'oldboy'
# name2 = 'oldboy'
# name1_id = id(name1)
# name2_id = id(name2)
# print(name1_id,name2_id)
# a = "this is a very long sentence"
# b = "this is a very long sentence"
# print(id(a),id(b))

# a = 257
# b = 257
# print(id(a),id(b))
#
# a1 = -5
# b1 = -5
# print(id(a1),id(b1))

# a = -6
# b = -6
# print(id(a),id(b))
#
# a1 = 259
# b1 = 259
# print(id(a1),id(b1))
# name1 = 'oldboy'
# name2 = name1
# name1 = 'alex'
# print(name1,name2)
# L1 = []
# L2 = ['a','b','c','d']

# product = [['iphone',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
# print("-----商品列表-----")
# for index,item in enumerate(product):
#     msg = "%s %s %s"%(index,product[index][0],product[index][-1])
#     print(msg)
# product = [['iphone',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
# print("-----商品列表-----")
# for index,item in enumerate(product):
#     msg = "%s %s %s"%(index,item[0],item[-1])
#     print(msg)


#
# product = [['iphone',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
# shopping_cart = []
# while True:
#     print("------商品列表------")
#     for index,i in enumerate(product):
#         print("%s  %s  %s"%(index,i[0],i[1]))
#     choose = input("输入商品编号（0-5），退出（q）")
#     if choose.isdigit():
#         choose =int(choose)
#         if choose < len(product):
#             shopping_cart.append(product[choose])
#             print("商品已加入购物车！%s" %(product[choose]))
#         else:
#             print("输入有误，商品不存在")
#     elif choose == 'q':
#         if len(shopping_cart) > 0:
#             print("-----你的购物车------")
#             for index ,p in enumerate(shopping_cart):
#                 print("%s   %s   %s   "%(index,p[0],p[1]))
#         break
#     else:
#         print("输入有误，请重新输入")

# import sys
# sum  = 10
# sum1 = ""
# print(sys.getsizeof(sum1))
#
# a = "lao"
# b = 'wang'
# c = a + b
# print(c)
#
# A = 10
# B = 2
# C = A + B
# print(C)
# #####################第一种方式
# e = "===" + a + b + "==="
# print(e)
# #####################第二种方式
# f = "===%s==="%(a+b)
# print(f)



# num = 100
# num2 = "100"
# name = 'alex'
#
# num3 = int(num2)
# print(type(num3),num3)
#
# num1 = str(num)
# print(type(num1),num1)
#
# print(len(name))

# name = "abcdef"
# print(name[0])
# print(name[5])
# print(name[6])
# print(name[len(name)-1])
# print(name[-1])
# print(name[-2])
# print(name[-3])
#   正向切片---顾头不顾尾
# name = "abcdefABCDEF"
# print(name[2:5]) #实质[2:4]
# print(name[2:6])#实质[2:5]
#
# #反向切片
# print(name[2:-2])
# print(name[2:-1])
# print(name[2:0])
# print(name[2:])
# print(name[2:-1])
# print(name[2:-1:2])
# print(name[2:-1:1])
# print(name[2:-1]) #默认步长为1
# print(name)
#  ## 正序
# print(name[0:])
#
# print(name[-1:])
#
# print(name[-1:0])
#####倒序
# print(name[-1:0:-1])
#
# print(name[-1::-1])
#
# print(name[::-1])
my_str = "hello world python and pythonxxxcpp"
# print(my_str.find("world")) #w的下标
# print(my_str.find("python"))#从左边开始find
# print(my_str.rfind("python"))#从右边开始find
# print(my_str.find("redhat"))#没有find out 返回-1

# print(my_str.index("python"))
# print(my_str.rindex("python"))
# print(my_str.index("redhat"))#没找到报错

######count
# print(my_str.count("python"))
# print(my_str.count("world"))
# print(my_str.count("redhat"))

######replace
# print(my_str.replace("world","WORLD"))
#
#
# print(my_str.replace("python","redhat",1))  #替换第一个
# print(my_str)
# print(my_str.split(" "))

# print(my_str.capitalize())
#
# print(my_str.title())


# file_name = 'abc.txt'
# print(file_name.endswith(".txt"))
# print(file_name.startswith("abc"))
# name = "Abc"
# print(name.lower())
#
# print(name.upper())
# lyric = "想要陪你一起看大海"
# print(lyric.center(50))
#
# print(lyric.ljust(50))
#
# print(lyric.rjust(50))
# lyric = "                   想要陪你一起看大海"
# print(lyric.lstrip()) #去除左\n,\t
# print(lyric.rstrip())#去除右\n,\t
# print(lyric.strip())#trip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

# print(my_str.partition("python"))
# print(my_str.rpartition("python"))

# my_line = "hello\nworld\nxx\nyy\nzz"
# print(my_line)
#
# print(my_line.splitlines())
#####数字整数  isdigit
# num = input("输入数字")
# if num.isdigit():
#     num = int(num)
#     print("是数字：",num)


######字母 isalpha
# num = input("输入内容：")
# if num.isalpha():
#     print("是字母",num)

####注册页面，必须是数字与字母的组合
# num = '1q'
# print(num.isdigit())
#
# print(num.isalpha())
#
# print(num.isalnum())

# num = input("输入内容:")
# if num.isalnum():
#     print("是字母和数字",num)
# a = ["aa","bb","cc"]
# print(a)
#
# b = "="
# print(b.join(a))
#
#
# b = " "
# print(b.join(a))


# s = "myname is {name}, i am {age}"
# # print(s.format("alex",22))
# print(s.format(name='alex',age=22))

# test_str = "hello world nihao \t heihie \t woshi nide\tpython \n ll\ndu"
# res = test_str.split()
#
# print(" ".join(res))
# print("".join(res))
# tuple1 = (11,22,33)
# print(type(tuple1))
#
# tuple1[0] = 99

a = (11,22)
b = a






