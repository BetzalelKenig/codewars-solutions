// Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).

// Consonants are letters used in English other than "a", "e", "i", "o", "u". We will count "y" as a consonant.

// Remember, your function needs to return the number of unique consonants - disregarding duplicates. For example, if the string passed into the function reads "add", the function should return 1 rather than 2, since "d" is a duplicate.

// Similarly, the function should also disregard duplicate consonants of differing cases. For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.

// Examples
// "add" ==> 1
// "Dad" ==> 1
// "aeiou" ==> 0
// "sillystring" ==> 7
// "abcdefghijklmnopqrstuvwxyz" ==> 21
// "Count my unique consonants!!" ==> 7

#include <ctype.h>
#include <stdbool.h>

// Count the number of unique consonants in a string
unsigned count_consonants(const char *str) {
    bool seen[256] = {false}; /* Seen characters */
    unsigned count = 0;

    for (const char *p = str; *p; p++) {
        // Convert character to lower case
        char c = tolower(*p);
        // Check if character is a consonant and has not been seen before
        if (isalpha(c) && c != 'a' && c != 'e' && c != 'i' && c != 'o' &&
            c != 'u' && !seen[c]) {
            seen[c] = true;
            count++;
        }
    }

    return count;
}