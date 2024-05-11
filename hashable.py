# Ramalho: "there is no way to make attributes really private and imuttable" 
# Imutability is essential for the object to be hashable

class Vector2d:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, x):
        return self.x == x.x and self.y == x.y

# a = Vector2d(10,20)
# a.__x = 11
# print(a.__x)

avect = Vector2d(2, 1)
bvect = Vector2d(2, 1)
adict = { avect : 'pointA', bvect: 'pointB'}

# print (adict)
# print ( avect is bvect )
# for i in avect:
#     print (i)

print (avect == bvect)

print (hash(avect), id(avect))
print (hash(bvect))

print (adict [ avect ] )


# create attributtes dinamycally, just curiosity nothing todo with hashes
# arecord = {'prop1':1, 'prop2':1.2}
# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
# rec = Record(**arecord)
# print(rec.prop1)
# print(rec.prop2)

