# Build Tower

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

#     Python: return a list;
#     JavaScript: returns an Array;
#     C#: returns a string[];
#     PHP: returns an array;
#     C++: returns a vector<string>;
#     Haskell: returns a [String];
#     Ruby: returns an Array;
#     Lua: returns a Table;

# Have fun!

# for example, a tower of 3 floors looks like below

# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]

# and a tower of 6 floors looks like below

# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]


def tower_builder(f):
    return [f"{' '*int(((f*2-1)-(n*2-1))/2)}{'*'*(n*2-1)}{' '*int(((f*2-1)-(n*2-1))/2)}" for n in range(1,f+1)]