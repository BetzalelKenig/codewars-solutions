// In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

// Examples:

// [1, -1, 2, -2, 3] => 3

// 3 has no matching negative appearance

// [-3, 1, 2, 3, -1, -4, -2] => -4

// -4 has no matching positive appearance

// [1, -1, 2, -2, 3, 3] => 3

// (the only-positive or only-negative integer may appear more than once)

// Good luck!

#include <stddef.h>

int solve(size_t n, const int array[n]) {

  for(size_t i = 0; i < n; i++){
    int check = 0;
    for(size_t j = 0; j < n; j++){
      if(array[j] == -array[i]){
        check = 1;
        break;  
      }
    }
    if(check == 0) return array[i];
  }
}