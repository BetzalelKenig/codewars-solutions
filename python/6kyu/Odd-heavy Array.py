# Array [11,4,9,2,8] is odd-heavy 
# because:- its odd elements [11,9] are greater than all the even elements [4,2,8]

# Array [11,4,9,2,3,10] is not odd-heavy
# because:- one of it's even element 10 from [4,2,10] is greater than two of its odd elements [9,3] from [ 11,9,3]

# write a function called isOddHeavy or is_odd_heavy that accepts an integer array and returns true if the array is odd-heavy else return false.

def is_odd_heavy(arr):
    odds = [i for i in arr if i % 2 != 0]
    if len(odds) == 0: return False
    evens = [i for i in arr if i % 2 == 0]
    if len(evens) == 0: return True
    return min(odds) > max(evens)