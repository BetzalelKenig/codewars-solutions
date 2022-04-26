// Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
// Examples (Input -> Output):

// * "String"      -> "SSttrriinngg"
// * "Hello World" -> "HHeelllloo  WWoorrlldd"
// * "1234!_ "     -> "11223344!!__  "

#include <string.h>

char *double_char (const char *string, char *doubled)
{
  *doubled = '\0'; // write to doubled
  for (int i = 0; i < strlen(string); i++) {
    doubled[i*2] = string[i];
    doubled[i*2+1] = string[i];
  }
  doubled[strlen(string)*2] = '\0';
  return doubled; // return it
}