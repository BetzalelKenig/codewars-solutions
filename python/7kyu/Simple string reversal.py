# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

# For example:

# solve("our code") = "edo cruo"
# -- Normal reversal without spaces is "edocruo". 
# -- However, there is a space after the first three characters, hence "edo cruo"

# solve("your code rocks") = "skco redo cruoy"
# solve("codewars") = "srawedoc"

# More examples in the test cases. All input will be lower case letters and in some cases spaces.

# Good lu

def solve(s):
    rev = s[::-1].replace(' ', '')
    res = ''
    j = 0
    for i in range(len(s)):
        if s[i] is ' ':
            res += ' '
        else:
            res += rev[j]
            j += 1
    return res