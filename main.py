import random
i=0
list=[1,2,3]
print(sum(i for i in list))
list2=[1,1,3,4,5,6]
print([item in list2 for item in list2])

a=[[0] * 4 for i in range(5)]
а=[[0 for j in range(4)] for i in range(5)]
print(a)

for i in range(4):
    print(' '.join(map(str,a[i])))

print("1:")
a = [[ i for j in range(6)] for i in range(5)]
for i in a:
 print (i)

print("2:")
a = [[ j for j in range(6)] for i in range(5)]
for i in a:
 print (i)

print("3:")
a = [[i+j for j in range(5)] for i in range(4)]
for i in a:
    print(i)

print("4:")
a = [[(j+i)%2 for j in range(5)] for i in range(4)]
for i in a:
 print (i)

dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_123 = {v: k for k, v in dict_abc.items()}
print(dict_abc)
print(dict_123)

tuplSurname='Mych','Yurts','Felyk'
print(tuplSurname)
tuplNum=tuple(random.randrange(1,100) for i in range(3))
print(tuplNum)
dictStud=dict(zip(tuplSurname,tuplNum))
print(dictStud)


