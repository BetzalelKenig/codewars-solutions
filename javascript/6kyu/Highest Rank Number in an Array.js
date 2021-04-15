// Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

// Note: no empty arrays will be given.
// Examples

// [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
// [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
// [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


function highestRank(arr) {
    let obj = {};
    arr.forEach((n) => {
      if (obj[n]) {
        obj[n]++;
      } else obj[n] = 1;
    });
    let sortable = [];
    for (let num in obj) {
      sortable.push([num, obj[num]]);
    }
    sortable.sort((x, y) => {
      let n = x[1] - y[1];
      if (n !== 0) {
        return n;
      }
  
      return x[0] - y[0];
    });
    return Number(sortable.reverse()[0][0]);
  }
