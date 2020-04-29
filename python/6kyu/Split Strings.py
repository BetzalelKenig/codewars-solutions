# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']


import re
def solution(s):
    return re.findall('..', s+'_')


from textwrap import wrap
def solution(s):
    r = wrap(s, 2)
    if len(s) % 2 == 1:
        r[-1] += '_'
    return r