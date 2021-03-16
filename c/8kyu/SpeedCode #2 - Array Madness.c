// SpeedCode #2 - Array Madness
// Objective
// Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

// E.g.

// array_madness(3, {4, 5, 6}, 3, {1, 2, 3}) == true;
// // because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3

#include <stdbool.h>
#include <stddef.h>

bool array_madness(size_t n1, const int arr1[n1], size_t n2, const int arr2[n2])
{

    int f = 0, s = 0;
    for (size_t i = 0; i < n1; i++)
    {
        f += arr1[i] * arr1[i];
    }
    for (size_t i = 0; i < n2; i++)
    {
        s += arr2[i] * arr2[i] * arr2[i];
    }
    return f > s;
}