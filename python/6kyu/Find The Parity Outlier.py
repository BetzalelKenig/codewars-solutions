# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# Examples

# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    
    def find(flag):
        for i in integers:
            if i % 2 == flag:
                return i
            
    first = integers[0]
    if integers[1]%2==integers[2]%2==0 and first%2 != 0: return first
    if integers[1]%2==integers[2]%2==1 and first%2 == 0: return first
    for i in range(1, len(integers)):
        if integers[i] % 2 == 0 and first % 2 == 0:
            return find(1)
        if integers[i] % 2 != 0 and first % 2 != 0:
            return find(0)