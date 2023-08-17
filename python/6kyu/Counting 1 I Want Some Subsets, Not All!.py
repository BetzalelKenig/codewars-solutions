# From the set S2 equals to[1,2,3], it is obvious that we have only 4 subsets and are:

# [1],[2],[3],[1,3]

# Make a code that may give the amount of all these subsets for any integer n >= 2    .

# Features of the random tests:

# number of tests = 100 
# 10 <= n <= 120

def f(n):
    if n < 3: return n
    n2 = 1
    n1 = 2
    for i in range(3, n+1):
        n1, n2 = n1 + n2 + 1, n1
    return n1