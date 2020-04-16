// Task

// Given a positive integer n, calculate the following sum:

// n + n/2 + n/4 + n/8 + ...

// All elements of the sum are the results of integer division.
// Example

// 25  =>  25 + 12 + 6 + 3 + 1 = 47


public class HalvingSum {
  int halvingSum(int n) {
    int sum = n; 
    for(int i = 2; n > 0; i *= 1){
      sum += n / i;
      n /= i;
    }
  return sum;    
  }