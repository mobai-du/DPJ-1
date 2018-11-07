#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

class Animal(object):#基类、父类、超类

    def run(self):
        print("Animal is running...")



class Dog(Animal):#子类
    def run(self):
        print("Dog is running ...")

    def eat(self):
        print("Eating meat...")
'''
注意：当子类与父类都存在相同的run()方法是，子类的run()覆盖父类的run()，
在代码运行时，总会调用子类。这就是继承的另一个好处——多态

'''
class Cat(Animal):
    def run(self):
        print("cat is running ...")
def run_twic(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twic(Tortoise())
'''
多态的好处就是，当我们需要传入dog,cat,tortoise...时,我们只需要接受Animal类型就可以了
因为dog,cat,tortoise...都是Animal类型，然后，安装Animal类型操作即可，由于Animal类型有
run()方法，因此，传入的任意类型。只要是Animal类或者子类，就会自动调用实际类型的run()方法，
这就是多态
'''

'''

'''
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
# run_twic(Animal())
# run_twic(Dog())
# run_twic(Cat())




class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()#测试对象的属性
# print(hasattr(obj,'x'))#有属性x吗？
# print(obj.x)
# print(hasattr(obj,'y'))#有属性y吗？
# setattr(obj,'y',19)
# print(hasattr(obj,'y'))
# print(getattr(obj,'y'))
# print(obj.y)
# # print(getattr(obj,'z'))
# print(getattr(obj,'z',404))

'''
获取对象的方法
hasattr():表示判断是否正确，是返回true，否返回flase
getattr():表示获取对象的属性
'''
print(hasattr(obj,'power'))
print(getattr(obj,'power'))#获取属性'power'
fn = getattr(obj,'power')#赋值
print(fn)#fn指向obj.power
print(fn())#调用

