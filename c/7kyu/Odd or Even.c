// Task:
// Given a list of integers, determine whether the sum of its elements is odd or even.

// Give your answer as a string matching "odd" or "even".

// If the input array is empty consider it as: [0] (array with a zero).

// Examples:
// Input: [0]
// Output: "even"

// Input: [0, 1, 4]
// Output: "odd"

// Input: [0, -1, -5]
// Output: "even"
// Have fun!

#include <stddef.h>

const char *odd_or_even(const int *v, size_t sz)
{
    int sum, i;
    for (i = 0; i < sz; i++)
        sum += v[i];
    return sum % 2 == 0 ? "even" : "odd";
}