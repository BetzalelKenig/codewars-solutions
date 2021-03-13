# Implement a function which behaves like the 'uniq -c' command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance together with the number of times a duplicate elements occurred in the original array.

# Example:

# ['a','a','b','b','c','a','b','c'] --> [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)]

def uniq_c(seq):
    if not seq: return []
    char, counter = seq[0], 1
    res = []
    for i in range(1, len(seq)):
        if seq[i] == char:
            counter += 1
        else:
            res.append((char, counter))
            char, counter = seq[i], 1
    res.append((char, counter))
    return res