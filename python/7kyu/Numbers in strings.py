# In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.

# For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

# Good luck!

import re
def solve(s):
    return max([int(x) for x in re.compile('\D').split(s) if x != ''])