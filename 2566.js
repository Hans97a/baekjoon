// let input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

// let a = 0,
//   b = 0;
// let max = 0;

// for (let i = 0; i < 9; i++) {
//   let line = input[i].split(" ").map((el) => Number(el));
//   for (let j = 0; j < 9; j++) {
//     if (line[j] > max) {
//       max = line[j];
//       a = i;
//       b = j;
//     }
//   }
// }
// console.log(max);
// console.log(a + 1, b + 1);
// let input = require("fs")
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .flat();

//   let a = 0,
//   b = 0;
// let max = 0;
// for (let i = 0; i < 9; i++) {
//   let line = input[i].split(" ").map((el) => Number(el));
//   for (let j = 0; j < 9; j++) {
//     if (line[j] > max) {
//       max = line[j];
//       a = i + 1;
//       b = j + 1;
//     }
//   }
// }
// console.log(max);
// console.log(a, b);

const fs = require("fs");
const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number))
  .flat();

const max = Math.max(...input);
const index = input.indexOf(max);

const row = Math.floor(index / 9) + 1;
const col = (index % 9) + 1;

console.log(max);
console.log(row, col);
