// In Racket, the function is called palindrome?

// (palindrome? "nope") ; returns #f
// (palindrome? "Yay")  ; returns #t

#include <stdbool.h>
#include <string.h>

bool is_palindrome(const char *str_in)
{
    for (int i = 0, j = strlen(str_in) - 1; i < (int)strlen(str_in) / 2; i++, j--)
    {
        if (str_in[i] != str_in[j] && str_in[i] + 32 != str_in[j])
            return false;
    }
    return true;
}
