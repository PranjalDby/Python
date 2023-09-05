# exception is a error which is of any type like syntax error  or runtime error
# try:
#     a= 10
#     a='str'
# except TypeError as e:
#     print(e)
# x =-5

# raise keyword
# if x<0:
#     raise Exception('x should be +')

# assert
# x =-5
# assert (x > 0),'x is not +'


class ValueTooHighError(Exception):
    pass

def test(x):
    if x>100:
        raise ValueTooHighError('Value Too high')


test(200)


