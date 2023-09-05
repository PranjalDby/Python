# dict are mutable key - value paired collection of element's with no two duplicate key are present
import timeit
dict = {}
lis = [22,34,56,78,90,100]
def get_key(elem,size):
    key = elem % size
    return key

size = len(lis)
print(get_key(22,size))
for i in range(size):
    dict.__setitem__(i,lis[i])

print(dict)
elem = int(input('enter the number: '))
flag = 0
# timeit.timeit('"".join(str)',number=100)

for i in range(len(dict)):
    if(elem == dict.get(i)):
        flag = 1
        break;

if flag == 1:
    print('yes')
else:
    print('Not found')







