# Take an input string and return a string that is made up of the number of occurances of each english letter in the input, followed by that letter. The string shouldn't contain zeros; leave them out.

# An empty string, or one with no letters, should return an empty string.

# Notes:

#     the input will always be valid;
#     treat letters as case-insensitive

# Examples

# "This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
# ""                          ==>  ""
# "555"                       ==>  ""


def string_letter_count(s):
    s = s.lower()
    ab = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in ab:
        if s.count(i):
            res += str(s.count(i)) + i
    return res