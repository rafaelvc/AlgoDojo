def add_one_decorator(f):
    def add_one(*args, **kwargs):
        if len(args) == 0: 
           print('arg none')
           return f() + 1
        return f(*args) + (args[0] + 1)
    return add_one

def force_an_argument(f):
    def check_args_and_run(*args):
        if len(args) == 0: 
            return f(1)
        return f(*args)
    return check_args_and_run

# a parametrized decorator
def force_an_argument_param(default=10):
    def decorate(f):
        def check_args_and_run(*args):
            if len(args) == 0: 
                return f(default)
            return f(*args)
        return check_args_and_run
    return decorate

@add_one_decorator
def f(a=1):
    return a

@force_an_argument
def g(a):
    return a

@force_an_argument_param(11)
def h(a):
    return a

@force_an_argument_param()
def i(a):
    return a


print (f(3))
print (g())
print (h())
print (h(5))
print (i())


