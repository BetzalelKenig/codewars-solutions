// In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

// Examples:

// permutations('a'); // ['a']
// permutations('ab'); // ['ab', 'ba']
// permutations('aabb'); // ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

function permutations(string) {
  let arr = [];
  if (string.length <= 1) {
    arr.push(string);
    return arr;
  }
  for (let i = 0; i < string.length; i++) {
    let char = string[i];
    let res = string.slice(0, i) + string.slice(i + 1, string.length);
    for (let p of permutations(res)) {
      arr.push(char + p);
    }
  }
  return arr.filter((e, i) => arr.indexOf(e) == i);
}
