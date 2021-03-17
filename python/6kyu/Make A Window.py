# Make me a window. I'll give you a number (N). You return a window.

# Rules:

# The window will always be 2 x 2.

# The window needs to have N number of periods across and N number of periods vertically in each pane.

# Example:

# N = 3

# ---------
# |...|...|
# |...|...|
# |...|...|
# |---+---|
# |...|...|
# |...|...|
# |...|...|
# ---------
# Note: there should be no trailing new line characters at the end.

def make_a_window(num):
    res = '-'*(num*2+3)+'\n'
    for i in range(num):
        res += '|'+'.'*num+'|'+'.'*num+'|'+'\n'
    res += '|'+'-'*num+'+'+'-'*num+'|'+'\n'
    for i in range(num):
        res += '|'+'.'*num+'|'+'.'*num+'|'+'\n'
    res += '-'*(num*2+3)
    return res
