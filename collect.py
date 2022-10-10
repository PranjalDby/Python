from collections import deque
# collections : counter ,namedtuple,orderdict,default dict , deque
# its stores value like dict key and count is like value

# a = "aaaaaaaaaaaabbbbbbbcccccccc"
# try:
#     my_counter = Counter(a)
#     print(my_counter)
#     # print(my_counter.most_common(3)[1][0])
#     print(list(my_counter.elements()))
# except ImportError as e:
#     print("erroro")

# ______________________________________________________________________________________
# named tuple
# Point = namedtuple('Point','x,y')
# pt = Point(1,-4)
# print(pt)

#________________________________________________________________
# oredered dict

# dicts = OrderedDict()
# dicts['a'] = 1
# dicts['b'] = 2
# print(dicts)

# default dict

# di = defaultdict(float)
# di['a'] = 1
# di['b'] = 2

# print(di['c'])

# deque
# double ended queue
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(4)
# d.pop()
# print(d)