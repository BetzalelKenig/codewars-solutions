# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)

# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)

# Happy coding! :)

def longest_repetition(chars):
    if chars == '':
        return ('', 0)
    longest = 0
    res = ''
    temp = 0
    char = chars[0]
    for i, e in enumerate(chars):
        if e == char:
            temp += 1
            if temp > longest:
                longest = temp
                res = e
        else:
            if i+1 < len(chars):
                char = e
            temp = 1
    return (res, longest)