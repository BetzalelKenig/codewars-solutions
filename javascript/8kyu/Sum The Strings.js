// Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

// Example: (Input1, Input2 -->Output)

// "4",  "5" --> "9"
// "34", "5" --> "39"

// If either input is an empty string, consider it as zero.

const sumStr = (a, b) => `${eval(`${a || 0}+${b || 0}`)}`;
