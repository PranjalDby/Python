invoice = """
0.....6.................................40........52...55........
1909   Pimoroni PiBrella                    $17.50 3 $52.50
1489   6mm Tactile Switch x20                $4.95 2 $9.90
1510   Panavise Jr. - PV-201                $28.00 1 $28.00
1601   PiTFT Mini Kit 320x240               $34.95 1 $34.95
"""

# using slice object
line_items = invoice.split('\n')[2:]

counted_space = 0
for item in line_items:
    print(f"{item[6:40]} {item[41:50]}")

# testing ...
# here when a is sequence containing mutable items,it will create three reffrences..
a,b,c = [[1,2,3]] * 3

print(c)
# sometimes it may be helpful ..

board = [['_'] * 3 for i in range(3) 
         for j in range(3)]

for i in board[:3]:
    board[1][1] = 'X'
    print(i)

print('Augmented assingments with sequences....')
a = [1,2,3,5]
b = [1,0,1,0]
a+=b
a[4] *= 3
# it's a deep copy
print(a)
print(b)
# while performing an multiplication and addition on immutable sequences it will create new copy of same target and then append it..
t = (1,2,[30,40])
try:
    t[2] += [50,60]
    print(t)
except TypeError as e:
    print(t)

# there is difference between list method .sort() and builtin sorted method is that
# .sort() does not create a new list it just return None if operaion perfom successfully


fruits =  ['grape', 'raspberry', 'apple', 'banana']
fruits.sort(key=str.lower)
print(fruits)
