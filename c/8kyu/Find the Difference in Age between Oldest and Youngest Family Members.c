// At the annual family gathering, the family likes to find the oldest living family member’s age and the youngest family member’s age and calculate the difference between them.

// You will be given an array of all the family members' ages, in any order. The ages will be given in whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with [youngest age, oldest age, difference between the youngest and oldest age].

#include <stdlib.h>

int *difference_in_ages(size_t a, const int ages[a])
{
    int *res = malloc(3);
    int min = ages[0], max = ages[0];
    for (size_t i = 0; i < a; i++)
    {
        if (ages[i] < min)
            min = ages[i];
        if (ages[i] > max)
            max = ages[i];
    }
    res[0] = min;
    res[1] = max;
    res[2] = max - min;
    return res;
}