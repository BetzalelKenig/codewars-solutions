# I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.

# Example: 

# n = 5;

# st = "This is an example string";

# Return value:
# Thisi
# sanex
# ample
# strin
# g

# Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'

def string_breakers(n, st):
    st = st.replace(' ', '')
    return '\n'.join([st[i:i+n] for i in range(0, len(st), n)])