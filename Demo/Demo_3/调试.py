f = open('information1.txt','r+')
date = f.readlines()
print(date)
while True:
    user_input = input(">>>").strip()
    if len(user_input) == 0:
        continue
    for line in date:
        if user_input in line:
            print(line.strip('\n'))
            break
