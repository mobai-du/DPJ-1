import pickle


# d = {'name':'alex','age':22}
#
# l = [1,2,3,4,'rain']
#
# pk = open("data.pkl","wb")
# pickle.dump(d,pk)
f = open("data.pkl","rb")
d = pickle.load(f)
print(d) 