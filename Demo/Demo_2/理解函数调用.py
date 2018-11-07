def func1():
    # age = 73
    # print(age)
    def func2():
        age = 84
        print(age)
    # func2()
# func1()
    func2()
#先定义在调用

def max(a,b):
    return a if a>b else b

def the_max(x,y,z):
    c = max(x,y)
    return max(c,z)
print(the_max(1,2,3))