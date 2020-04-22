// 

const decrypt = (str) => str.replace(/'(\d+)'/g, (_, x) => String.fromCharCode(x)).split('').reverse().join('');
