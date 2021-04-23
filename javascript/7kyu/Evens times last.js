// Given a sequence of integers, return the sum of all the integers that have an even index, multiplied by the integer at the last index.

// If the sequence is empty, you should return 0.

function evenLast(numbers) {
  let res = 0,
    last = numbers[numbers.length - 1];
  for (let i = 0; i < numbers.length; i += 2) {
    res += numbers[i] * last;
  }
  return res;
}
