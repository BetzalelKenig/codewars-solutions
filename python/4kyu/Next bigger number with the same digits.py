# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071

# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

# def next_bigger(n):
#     s = list(str(n))
#     if n in range(10):
#         return -1
#     i = len(s) -1
#     while i > 0:
#         if s[i] > s[i-1]:
#             s[i-1], s[i] = s[i], s[i-1]
#             temp = int(''.join(s))
#             j = len(s) - 1
#             while j >= i - 1:
#                 s[i-1], s[i] = s[i], s[i-1]
#                 j -= 1
#             return max(int(''.join(s)), temp)
#         i -= 1
#     return -1


def next_bigger(n):    
    s = list(str(n))
    i = len(s) - 1
    if n < 10 or i == 0:
        return - 1
    while i >= 1 and s[i-1] >= s[i]:
        i -= 1
    if i == 0:
        return -1      
    temp, pos = len(s) - 1, s[i-1]
    while pos >= s[temp]:
        temp -= 1
    s[temp], s[i-1] = s[i-1], s[temp]
    s[i:] = s[:i-1:-1]
    return int(''.join(s))
    