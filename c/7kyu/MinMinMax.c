// Given an unsorted array of integers, find the smallest number in the array,
// the largest number in the array, and the smallest number between the two
// array bounds that is not in the array.

// For instance, given the array [-1, 4, 5, -23, 24], the smallest number is
// -23, the largest number is 24, and the smallest number between the array
// bounds is -22. You may assume the input is well-formed.

// You solution should return an array [smallest, minimumAbsent, largest]

// The smallest integer should be the integer from the array with the lowest
// value.

// The largest integer should be the integer from the array with the highest
// value.

// The minimumAbsent is the smallest number between the largest and the smallest
// number that is not in the array.

// min_min_max({-1, 4, 5, -23, 24}, 5);    //  {-23, -22, 24}
// min_min_max({1, 3, -3, -2, 8, -1}, 6);  //  {-3, 0, 8}
// min_min_max({2, -4, 8, -5, 9, 7}, 6);   //  {-5, -3, 9}

#include <stdbool.h>
#include <stdlib.h>
//  function returns user allocated int array
//  output memory will be freed by the tester

int *min_min_max(const int *array, size_t n) {
    int *result = malloc(3 * sizeof(int));

    /* Initialize the result values */
    result[0] = result[1] = result[2] = array[0];

    /* Find the smallest, minimum absent, and largest numbers */
    for (size_t i = 1; i < n; i++) {
        if (array[i] < result[0]) {
            result[0] = array[i];
        }
        if (array[i] > result[2]) {
            result[2] = array[i];
        }
    }
    for (int i = result[0] + 1; i < result[2]; i++) {
        bool found = false;
        for (size_t j = 0; j < n; j++) {
            if (array[j] == i) {
                found = true;
                break;
            }
        }
        if (!found) {
            result[1] = i;
            break;
        }
    }

    return result;
}