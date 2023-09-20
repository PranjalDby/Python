import timeit
from decorators_utils import timer
ls = [1,6,4,2,8,10,13,56,333]

@timer
def calc_max():
    for i in range(len(ls)-1):
        max = ls[i]
        if max <= ls[i+1]:
            max = ls[i+1]

    print(max)

max = calc_max()
print(max)