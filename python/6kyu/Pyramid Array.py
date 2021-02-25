# Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

# pyramid(0) => [ ]
# pyramid(1) => [ [1] ]
# pyramid(2) => [ [1], [1, 1] ]
# pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

# Note: the subarrays should be filled with 1s

def pyramid(n):
    return [[1 for i in range(j)] for j in range(1,n+1)]