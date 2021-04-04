# Write a function with the signature shown below:

# def is_int_array(arr):
#     return True

#     returns true / True if every element in an array is an integer or a float with no decimals.
#     returns true / True if array is empty.
#     returns false / False for every other input.


def is_int_array(arr):
    if not isinstance(arr, list) or None in arr: return False
    if not arr: return True
    for i in arr:
        if not isinstance(i, (int, float)) or i % 1 != 0:
            return False
    return True