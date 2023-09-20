import functools
import time

def do_twice(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('doing second call')
        func(*args,**kwargs)
    
    return wrapper

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        value = func(*args,**kwargs)
        return value
    
    return wrapper


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

def debugging(func):
    
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        func_signature = ", ".join(args_repr+kwargs_repr)
        print(f"Calling {func.__name__}({func_signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    
    return wrapper

def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args,**kwargs)

        return wrapper.instance
    
    wrapper.instance = None    
    return wrapper

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.noc +=1
        print(f"Call {wrapper.noc} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper.noc = 0
    return wrapper

def repeat(func=None,*,n_times=2):
    def decorator_rr(func):
        def wrapper(*args,**kwargs):
            for _ in range(n_times):
                func(*args,**kwargs)
        return wrapper
    
    if func == None:
        decorator_rr
    
    else:
        decorator_rr(func)
    return decorator_rr

