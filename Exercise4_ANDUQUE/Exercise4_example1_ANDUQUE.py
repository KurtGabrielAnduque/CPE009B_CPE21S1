class foo:
    def __init__(self,a,b):
        self._a = a
        self._b = b
        
    def add(self):
        return  self._a + self._b


object_foo = foo(3,4)
print(object_foo.add())

