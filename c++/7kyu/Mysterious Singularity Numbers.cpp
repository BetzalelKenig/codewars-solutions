// This is a rather simple but interesting kata. Try to solve it using logic. The shortest solution can be fit into one line.

// Task
// The point is that a natural number N (1 <= N <= 10^9) is given. You need to write a function which finds the number of natural numbers not exceeding N and not divided by any of the numbers [2, 3, 5].

// Example
// Let's take the number 5 as an example:

// 1 - doesn't divide integer by 2, 3, and 5
// 2 - divides integer by 2
// 3 - divides integer by 3
// 4 - divides integer by 2
// 5 - divides integer by 5
// Answer: 1

// because only one number doesn't divide integer by any of 2, 3, 5

// Note
// Again, try to think of a formula that will shorten your solution and help you pass big tests.

// This solution computes the number of natural numbers not exceeding N and divisible by 2, 3, or 5, and subtracts it from N to get the number of natural numbers not exceeding N and not divisible by any of these numbers.
// The formula uses integer division to compute the number of multiples of each prime number less than or equal to N, and then applies the principle of inclusion-exclusion to compute the number of multiples of any combination of these numbers.

unsigned int realNumbers(unsigned int n) {
  return n - (n/2 + n/3 + n/5 - n/6 - n/10 - n/15 + n/30);
}