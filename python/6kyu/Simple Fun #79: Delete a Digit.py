# Task

# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.
# Example

# For n = 152, the output should be 52;

# For n = 1001, the output should be 101.
# Input/Output

#     [input] integer n

#     Constraints: 10 ≤ n ≤ 1000000.

#     [output] an integer

def delete_digit(n):
    res = 0
    for l in str(n):
        if int(str(n).replace(l, '', 1)) > res:
            res = int(str(n).replace(l, '', 1))
    return res