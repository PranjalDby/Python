class Decorators:
    def __init__(self,func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func(*args,**kwargs)
        return res

@Decorators
def name(name,mess='hello'):
    print("{}{}".format(mess,name))

@Decorators
def sqr(num):
    return num * num

print(sqr(6))


