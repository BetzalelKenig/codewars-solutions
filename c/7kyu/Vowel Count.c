// Return the number (count) of vowels in the given string.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input string will only consist of lower case letters and/or spaces.

#include <stddef.h>

size_t get_count(const char *s)
{
  int count = 0;
  for(int i = 0; i<strlen(s); i++){
    if(s[i] == 97 || s[i] == 101 || s[i] == 105 || s[i] == 111 || s[i] == 117){
      count++;
    }
  }
    return count;
}