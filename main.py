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

print()
a = [[ i for j in range(6)] for i in range(5)]
for i in a:
 print (i)

print()
a = [[ j for j in range(6)] for i in range(5)]
for i in a:
 print (i)

print()
a = [[i+j for j in range(5)] for i in range(4)]
for i in a:
    print(i)

print()
a = [[ j%10 for j in range(5)] for i in range(4)]
for i in a:
 print (i)
