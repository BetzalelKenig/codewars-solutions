# In Python, == tests for equality and is tests for identity. Two strings that are equal may also be identical, but this is not guaranteed, but rather an implementation detail. Given a computed expression, ensure that it is identical to the corresponding equal string literal by completing the make_identical function. See test case for clarity. (Note, this is easy if you know the concept.)

from sys import intern
def make_identical(strng):
    return intern(strng)