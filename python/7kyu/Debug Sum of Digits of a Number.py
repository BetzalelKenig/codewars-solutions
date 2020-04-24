# Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.
# Example

# 123  => 6
# 223  => 7
# 1337 => 15



import functools
# def get_sum_of_digits(num):
#     sum = 0
#     digits = str(num)
#     for x in digits:
#         sum += int(x)
#     return sum


# def get_sum_of_digits(num):   
#     return functools.reduce(lambda a,b : a+b,[int(x) for x in str(num)] )


def get_sum_of_digits(num):
	return sum(map(int, str(num)))