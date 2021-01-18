// I love Fibonacci numbers in general, but I must admit I love some more than others.

// I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

// For example:

//    nthFibo(4) == 2

// Because 2 is the 4th number in the Fibonacci Sequence.

// For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.

function nthFibo(n, obj = {}) {
    if(n == 1)return 0
    if(n  in obj) return obj[n];
    if (n <= 2) return 1;
    obj[n] = nthFibo(n-1, obj) + nthFibo(n-2, obj);
    return obj[n]
  }