// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

// Examples:

// solution('abc', 'bc') // returns true
// solution('abc', 'd') // returns false

#include <stdbool.h>
#include <string.h>

bool solution(const char *string, const char *ending)
{
  int i = strlen(ending);
  int j = strlen(string);
  if(i > j) return false;
  for(;i >= 0; i--,j--){
    if(!(strcmp(&string[j], &ending[i])==0)) return false;
  }
    return true;
}