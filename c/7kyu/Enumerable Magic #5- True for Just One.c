// Task
// Create a function called one that accepts two params:

// a sequence
// a function
// and returns true only if the function in the params returns true for exactly one (1) item in the sequence.

// Example
// one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
// one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
// one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false

#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool one(const int *arr, size_t size, Predicate fun)
{
    int one = 0;
    for (int i = 0; i < size; i++)
    {
        if (fun(arr[i]))
            one++;
    }
    return one == 1;
}