let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((el) => Number(el));

let ave = input.reduce((a, b) => a + b, 0) / input.length;
let middle = input.sort((a, b) => a - b)[2];

console.log(ave);
console.log(middle);

// let input = require("fs")
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .split("\n").map(el => Number(el));

// let ave = input.reduce((a,b)=> a+b, 0) / input.length;
// let middle = input.sort((a,b) => a-b)[2];

// console.log(ave);
// console.log(middle);
