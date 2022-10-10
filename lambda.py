# syntax lambda aurgumnets expression

from traceback import print_tb


add10 = lambda x: x+10
print(add10(5))

muitl = lambda x,y:x * y
print(muitl( x = 3,y=4))


point2d = [(1,2),(13,1),(5,-1),(17,8)]
point2d_sort = sorted(point2d,key=lambda x: x[0] + x[1])
print(point2d_sort)
# map function
a = [1,2,3,4,5]
b = map(lambda x: x* 2,a)
print(list(b))