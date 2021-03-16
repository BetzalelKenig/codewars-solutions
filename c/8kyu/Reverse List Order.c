// In this kata you will create a function that takes in a list and returns a list with the reverse order.

// Examples
// reverse_list((int[]){1,2,3,4},4) == (int[]){4,3,2,1}
// reverse_list((int[]){3,1,5,4},4) == (int[]){4,5,1,3}

#include <stdlib.h>

int *reverse_list(const int *array, size_t length)
{
    int *arr = malloc(length * sizeof(int));
    for (size_t i = 0; i < length; i++)
    {
        arr[i] = array[length - i - 1];
    }
    return arr;
}