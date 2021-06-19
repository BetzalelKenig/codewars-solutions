# Update the solution method to round the argument value to the closest precision of two. The argument will always be a float.

# solution(23.23456) # should == 23.23
# solution(1.546) # should == 1.55

def solution(n):
    return round(n, 2)