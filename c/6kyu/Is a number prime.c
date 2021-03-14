// Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

// Requirements
// You can assume you will be given an integer input.
// You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
// NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.
// Example
// is_prime(1)  /* false */
// is_prime(2)  /* true  */
// is_prime(-1) /* false */

#include <stdbool.h>

bool is_prime(int num)
{
    if (num < 2)
        return false;
    if (num == 2 || num == 3)
        return true;
    int lim = ceil(sqrt(num)) + 1;

    for (int i = 2; i < lim; i++)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}