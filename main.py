import random
a=1234
print(sum(list(map(int, list(str(a))))))
print(sum([int(i) for i in str(a)]))

list2=[1,1,3,4,5,6]
print(len(list2)==len(set(list2)))

c="dsakf jasljgaklsg jaslkf"
print(len(set(''.join(c.split()))))

d={'r':5, 'y':2,'u':5,'p':2,'d':1}
print(list(d.values()).count(5))
d={'r':5, 'y':2,'u':5,'p':2,'d':1}
print(len([i for i in d.values() if i<3]))

h='ashjhfajsk.jhasfj?afs!,,,asgaghgasf'
print(''.join([i for i in h if not i in '.,/\!%;:?']))


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
a = [[(j+i+1)%2 for j in range(5)] for i in range(4)]
for i in a:
 print (i)

print("5:")
a = [[max(i,j) for j in range(5)] for i in range(4)]
for i in a:
     print(i)

print("5:")
a = [[1 if i==j or i+j==5 else 0 for j in range(5)] for i in range(4)]
for i in a:
     print(i)


print("4:")
w=iter(range(1,100))
a = [[next(w) if (j+i+1)%2==1 else 0 for j in range(5)] for i in range(4)]
for i in a:
 print (i)


dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_123 = {v: k for k, v in dict_abc.items()}
print(dict_123)

tuplSurname='Mych','Yurts','Felyk'
tuplNum=tuple(random.randrange(1,100) for i in range(3))
dictStud={tuplSurname[i]:tuplNum[i] for i in range(len(tuplNum))}
print(dictStud)


print([i+j+c for i in '010' for j in '001' for c in '100' ])


