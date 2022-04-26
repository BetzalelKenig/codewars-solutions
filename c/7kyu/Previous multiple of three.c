// Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.

// Return n if the input is already a multiple of three, and return -1 if no such number exists.
// Examples

// 1      => -1
// 25     => -1
// 36     => 36
// 1244   => 12
// 952406 => 9

#include <sys/types.h>

ssize_t prev_mult_of_three(ssize_t n) {
  while (n > 2) {
    if (n % 3 == 0) return n;
    n /= 10;
  }
  return -1;
}