# Implement a function which behaves like the uniq command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

# Example:

# ['a','a','b','b','c','a','b','c'] --> ['a','b','c','a','b','c']

def uniq(seq):
    if not seq: return []
    u = [seq[0]]
    for i in seq:
        if u[-1] != i:
            u.append(i)
    return u
