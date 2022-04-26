// Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

// Find the number of Friday 13th in the given year.

// Input: Year in Gregorian calendar as integer.

// Output: Number of Black Fridays in the year as an integer.

// Examples:

// unluckyDays(2015) == 3
// unluckyDays(1986) == 1

#include <string.h>

int unlucky_days(int year) {
  int weekday, results = 0;
  for (int m = 1; m < 13; m++) {
    int d = 13, y = year;
    weekday  = (d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7; 
    if (weekday == 5) results++;
  }
  return results;
}