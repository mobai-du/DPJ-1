products = [['iphone',6888],['macpro',14800],['xiaomi6',2499],['coffee',31],['book',80],['nike shoes',799]]
shopping_cart = []
while True:
    print("---------商品列表--------------")
    for index,p in enumerate(products):
        print("%s    %s    %s   "%(index,p[0],p[1]))
    choice = input("输入你要购买的商品（0-5/q退出）：")
    if choice.isdigit():
        choice=int(choice)
        if choice < len(products):
            shopping_cart.append(products[choice])
            print("商品已加入购物车"%(products[choice]))
        else:
            print("商品不存在")
    elif choice == 'q':
        if len(shopping_cart)>0:
            print("--------已购买如下商品------------")
            for index,p in enumerate(shopping_cart):
                print("%s  %s  %s "%(index,p[0],p[1]))
        break
    else:
        print("输入有误，请重新输入")
