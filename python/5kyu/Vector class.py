# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception

# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

# Also provide:

#     a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
#     an equals method, to check that two vectors that have the same components are equal

# Note: the test cases will utilize the user-provided equals method.

from math import sqrt

class Vector:
    data = ()
    def __init__(self, args):
        self.data = args
    
    def add(self, vec):
        self.validate(vec)
        print(self.data,vec.data)
        return Vector([i[0]+i[1] for i in zip(self.data, vec.data)])
            
    def subtract(self, vec):
        self.validate(vec)
        print(list(zip(self.data,vec.data)))
        return Vector([i[0]-i[1] for i in zip(self.data, vec.data)])
    
    def dot(self, vec):
        self.validate(vec)
        return sum([i[0]*i[1] for i in zip(self.data, vec.data)])
    
    def norm(self):
        return sqrt(sum([i**2 for i in self.data]))
            
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return f'({",".join([str(i) for i in self.data])})'
    
    def equals(self, vec):
        return self.data == vec.data
            
    def validate(self, vec):
        if len(vec) != len(self.data):
            raise Exception("Can't excute function on vectors with different length")