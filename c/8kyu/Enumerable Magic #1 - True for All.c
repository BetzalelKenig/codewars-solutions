// Create a method all which takes an array and a predicate (function pointer), and returns true if the predicate returns true for every element in the array. Otherwise, it should return false. If the array is empty, it should return true, since technically nothing failed the test.

#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool all(int *arr, size_t size, Predicate fun)
{
    for (int i = 0; i < size; i++)
    {
        if (!fun(arr[i]))
            return false;
    }
    return true;
}