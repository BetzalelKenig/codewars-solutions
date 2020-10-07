# Task

# Given a string str, reverse it omitting all non-alphabetic characters.
# Example

# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".
# Input/Output

#     [input] string str

#     A string consists of lowercase latin letters, digits and symbols.

#     [output] a string


def reverse_letter(string):
    res = ''
    for i in range(len(string)-1, -1, -1):
        if string[i] in 'abcdefghijklmnopqrstuvwxyz':
            res += string[i]
    return res

    

# def reverse_letter(string):
#     return ''.join(c for c in string[::-1] if c.isalpha())
    