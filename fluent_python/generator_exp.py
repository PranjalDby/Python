import array
# genexpes
"""
genexp (generator expression) saves memory because it yields items
one by one using the iterator protocol instead of building a whole list just to feed
another constructor
"""
symbols = '$¢£¥€¤'
tup = tuple(ord(s) for s in symbols)
print(tup)
"""                       generator expression                 
..........................|
------------------------  \/"""
array.array('I',(ord(s) for s in symbols))

# building cartesian product
colors = ['black','white','Red']
sizes = ['S','M','L']
for tshirts_color,tshirts_size in ((color,size) for color in colors for size in sizes):
    print("{} {}".format(tshirts_color,tshirts_size))


# Tuples as Records
# Tuples hold records: 
# each item in the tuple holds the data for one field, and the posi‐
# tion of the item gives its meaning.
print("tuples used as records...")
lax_coordinates = (33.942,-118.408056)
city,year,pop,chg,area = ('Tokiyo',2003,32_450,0.66,8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
print(traveler_ids[0][1])
for passport in sorted(traveler_ids):
    print("%s/%s"%passport)

# talking about immutability of tuple

tup = (1,2,colors)
print(tup)

def is_hashable(obj):
    try:
        hash(obj)
    
    except TypeError as e:
        return False
    
    return True

print(is_hashable(tup))

# nested unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

a,b,c,(d,e)= metro_areas[0]

for name,_,_,(lat,long) in metro_areas:
    if long <=0:
        print(f'{name:15} | {lat:9.4f} | {long:9.4f}')
