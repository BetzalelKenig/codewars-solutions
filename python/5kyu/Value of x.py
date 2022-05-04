# Jack's teacher gave him a ton of equations for homework. The thing is they are all kind of same so they are boring.

# So help him by making a equation solving function that will return the value of x.

# Test Cases will be like this:

# # INPUT            # RETURN
# 'x + 1 = 9 - 2'    # 6
# '- 10 = x'         # -10
# 'x - 2 + 3 = 2'    # 1
# '- x = - 1'        # 1

#     All test cases are valid.
#     Every +, - and numbers will be separated by space.
#     There will be only one x either on the left or right.
#     x can have a - mark before it.
#     returned object will be a integer.

def solve(eq: str):
    res = 0
    left, right = eq.split('=')
    left = left.split()
    right = right.split()
    
    for i, v in enumerate(left):
        if v in '-+':
            op = left.pop(i)
            left[i] = v+left[i]
            
    for i, v in enumerate(right):
        if v in '-+':
            op = right.pop(i)
            right[i] = v+right[i]
            
    with_x = []
    without_x = ''
    
    if 'x' in ''.join(left):
        without_x = ''.join(right)
        with_x = left
    else: 
        without_x = ''.join(left)
        with_x = right
        
    res = eval(without_x)
    
    for i, v in enumerate(with_x):
        if 'x' not in v:
            res += int(v) * -1
            
    if len([1 for i in with_x if '-x' in i]) == 1: res = res*-1
    
    return res