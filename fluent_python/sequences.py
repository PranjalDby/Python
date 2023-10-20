import array
import time
import functools
# container sequences holds the refference to the object it contains
# flat sequences holds the raw value of its own memory space

# example a tuple of float is a container
def timer(func=None):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:.4f}s")
        return value
    
    if func is None:
       return None
    
    else:
       return wrapper
float_tuple = (2.3,4.5,6.2,7.1)
print(type(float_tuple))

arr_float = array.array('f',[2.3,4.5,6.2,7.1])
print(arr_float)

# List Comprehension and generator experession

symbols = "$¢£¥€¤"
x = "@$%"
unicode_code = [ord(x) for x in x]
print(unicode_code)


x = 'ABC'

# assingning a varible using walrus operator :=
codes = [last:= ord(c) for c in x]
print(last)

print("List comprehension vs map and filter:::")
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
@timer
def list_comps():
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    return beyond_ascii

@timer
def using_filter_object():
    beyond_ascii = list(filter(lambda c : c > 127,map(ord,symbols)))
    return beyond_ascii


print(list_comps())
print("by using filtere'd method")
print(using_filter_object())
print(beyond_ascii)

colors = ['black','white']
sizes = ['S','M','L']
t_shirts = [(size,color) for color in colors 
            for size in sizes]
print(t_shirts)