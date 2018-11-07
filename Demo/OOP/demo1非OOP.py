#!/usr/bin/env python 
#$ coding:utf-8 $
#__Author__:Peter Du

# #role 1
# name = 'alex'
# role = 'terrorrist'
# weapon = 'ak47'
# life_value = 100
# money = 10000
#
# #role 2
# name2 = 'jack'
# role2 = 'police'
# weapon2 = 'b22'
# life_value2 = 100
# money2 = 10000
#
# #role 3
# name2 = 'rain'
# role2 = 'terrorist'
# weapon2 = 'c33'
# life_value2 = 100
# money2 = 10000
#
# #role 4
# name2 = 'eric'
# role2 = 'police'
# weapon2 = 'b51'
# life_value2 = 100
# money2 = 10000


roles = {
    1:{'name':'alex',
       'role':'terrorist',
       'weapon':'ak47',
       'life_value':100,
       'money':15000,
       },
    2:{'name':'jack',
       'role':'police',
       'weapon':'b22',
       'life_value':100,
       'money':15000,
        },
    3:{'name':'rain',
       'role':'terrorist',
       'weapon':'c33',
       'life_value':100,
       'money':15000,
        },
    4:{'name':'eric',
       'role':'police',
       'weapon':'b51',
       'life_value':100,
       'money':15000,
        },
}

print(roles[1])
print(roles[2])

def shot(by_who):
    #开枪后子弹数减少
    pass
def got_shot(who):
    #中枪后要掉血
    who['life_value'] -= 10
    pass
def buy_gun(who,gun_name):
    #检查钱够不够，买了抢后扣钱
    pass