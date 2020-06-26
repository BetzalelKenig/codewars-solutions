# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

def capitalize(s):
    res1 = ''
    res2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            res1 += s[i].upper()
            res2 += s[i]
        else:
            res1 += s[i]
            res2 += s[i].upper()
    return [res1, res2]
