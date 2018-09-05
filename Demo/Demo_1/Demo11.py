users = [['alex','alex123'],#管理员
         ['pizza','pizza123'],#教师
         ['john','john123']]#学生
username = input("输入用户名")
password = input("输入密码")

if [username,password] == users[0]:
    print('登录成功')