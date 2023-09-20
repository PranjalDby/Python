
from math import asin, cos, radians, sin, sqrt
import sys,pathlib
# walrus operator := it used to assign the value to the variable in same expression

if data:=45:
    print(data)
# Approximate radius of Earth in kilometers
rad = 6371

# Locations of Oslo and Vancouver
ϕ1, λ1 = radians(59.9), radians(10.8)
ϕ2, λ2 = radians(49.3), radians(-123.1)

# Distance between Oslo and Vancouver
dis= 2 * rad * asin(
    sqrt(
        hav_sin:=sin((ϕ2 - ϕ1) / 2) ** 2
        + cos(ϕ1) * cos(ϕ2) * sin((λ2 - λ1) / 2) ** 2
    )
)
print(hav_sin)

# using in  list comprehensions

list_ = [10,20,30,11,9]

dicts = {
    'length': (leng:=len(list_)),
    'sums': (sums :=sum(list_)),
    'mean':sums/leng
    }

print(leng)
print(dicts)

file_path = pathlib.Path('python_extras/exap.txt')

counts = (
    (rd_text:=file_path.read_text()).count('\n'),
    len(rd_text.split()),
    rd_text
)
print(*counts)

numbers = [7,18,9,1,4,3,1]
def slow(num):
    return num ** 3
res = [slow(numbers) for numbers in numbers if slow(numbers) > 100]

filt = filter(lambda numbers:numbers > 0,(slow(nums) for nums in numbers))
print(list(filt))
print(res)
cities = ["Vancouver", "Oslo", "Houston", "Warsaw", "Graz", "Holguín"]

print(any(city.startswith('H') for city in cities))
if any((witness:=city).startswith('H') for city in cities):
    print(f'city starts with (H) is {witness}')