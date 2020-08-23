// It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

// Return the average of the given array rounded down to its nearest integer.

// The array will never be empty.

getAverage = (marks) =>
  Math.floor(marks.reduce((s, el) => s + el, 0) / marks.length);
