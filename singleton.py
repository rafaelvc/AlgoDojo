class SingletonClass:

    class Single:
        def __init__(self, x):
            self.x = x
        def test(self, x):
            return self.x + x

    singleton = None
    def __new__(self, *args, **kwargs):
        if self.singleton is None:
             self.singleton = SingletonClass.Single(*args, **kwargs)
        return self.singleton

test = SingletonClass(10)
test2 = SingletonClass()
 
print (test is test2) # true
print(test.x)
test.x = 11
print(test.x)
print(test2.x)