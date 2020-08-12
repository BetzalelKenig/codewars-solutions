# Task

# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:
# Street

# 1|   |6
# 3|   |4
# 5|   |2

# Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
# Example

# Given your house number address and length of street n, give the house number on the opposite side of the street.

# over_the_road(address, n)
# over_the_road(1, 3) = 6
# over_the_road(3, 3) = 4
# over_the_road(2, 3) = 5
# over_the_road(3, 5) = 8

# Both n and address could get upto 500 billion with over 200 random tests.

def over_the_road(a, n):
    return n*2+1-a
   
# def over_the_road(a, n):
#     odd = [i for i in range(1, n*2+1, 2)]
#     even = [i for i in range(n*2, 0, -2)]
#     if a % 2 != 0:
#         return even[odd.index(a)]
#     else:
#         return odd[even.index(a)]