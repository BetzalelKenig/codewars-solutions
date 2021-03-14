// Bob is a lazy man.

// He needs you to create a method that can determine how many letters and digits are in a given string.

// Example:

// "hel2!lo" --> 6

// "wicked .. !" --> 6

// "!?..A" --> 1

#include <stddef.h>

size_t count_letters_and_digits(const char *input)
{
    int res = 0, i = 0;

    while (input[i] != '\0')
    {
        if ((input[i] >= 'a' && input[i] <= 'z') || (input[i] >= 'A' && input[i] <= 'Z') || input[i] >= '0' && input[i] <= '9')
        {
            res++;
        }
        i++;
    }
    return res;
}