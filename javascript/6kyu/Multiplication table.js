// Your task, is to create NxN multiplication table, of size provided in parameter.

// for example, when given size is 3:

// 1 2 3
// 2 4 6
// 3 6 9
// for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

multiplicationTable = function (size) {
  let res = [];
  for (let i = 0; i < size; i++) {
    res[i] = [];
    for (let j = 0; j < size; j++) {
      res[i].push((i + 1) * (j + 1));
    }
  }
  return res;
};
