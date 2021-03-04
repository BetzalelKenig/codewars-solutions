# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

#     i increments the value (initially 0)
#     d decrements the value
#     s squares the value
#     o outputs the value into the return array

# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    res, x = [], 0
    for i in data:
        if i is 'i': x+=1
        if i is 'd': x-=1
        if i is 's': x*=x
        if i is 'o': res.append(x)
    return res
        