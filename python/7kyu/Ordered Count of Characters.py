# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

# Example:

# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]


def ordered_count(inp):
    return [(j,inp.count(j)) for i, j in enumerate(inp) if j not in inp[:i]]