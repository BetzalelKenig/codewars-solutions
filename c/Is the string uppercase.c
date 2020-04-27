// Is the string uppercase?
// Task

// Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

// is_uppercase("c") == false
// is_uppercase("C") == true
// is_uppercase("hello I AM DONALD") == false
// is_uppercase("HELLO I AM DONALD") == true
// is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == false
// is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == true

// In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.


#include <stdbool.h>

bool is_uppercase(const char *source){
  for (int i = 0; source[i] != 0; i++){
    if(source[i] > 96 && source[i] < 123) return false;
  }
  return true;
}