# product combination ,permutation,accumalte,groupby and infinite and this are iteratble tools
from itertools import count,cycle,repeat


# prod = product(a , b)
# print(list(prod))
# permutations
# per = permutations(a,2)
# print(list(per))
a = [1,2,3,4]
# def smaller(x):
#     return x < 3
# acuu  = groupby(a,key=lambda x: x<3)

# for key,value in acuu:
#     print(key,list(value))

# combinations
# comb = combinations(a,2)
# print(list(comb))

# lambda functions
for i in repeat(1,9):
    print(i)
