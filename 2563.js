// let input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

// let num = parseInt(input[0]);

// let arr = [];
// for (let i = 0; i < 100; i++) {
//   let temp = [];
//   for (let j = 0; j < 100; j++) {
//     temp.push(0);
//   }
//   arr.push(temp);
// }

// for (let i = 1; i <= num; i++) {
//   let [row, col] = input[i].split(" ").map((el) => Number(el));

//   for (let j = row; j < row + 10; j++) {
//     for (let k = col; k < col + 10; k++) {
//       arr[j][k] = 1;
//     }
//   }
// }

// let count = 0;

// for (let el of arr) {
//   for (let num of el) {
//     if (num === 1) count++;
//   }
// }
// console.log(count);

// let input = require("fs")
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .trim()
//   .split("\n");

// let num = parseInt(input[0]);

// let arr = [];
// for (let i = 0; i < 100; i++) {
//   let temp = [];
//   for (let j = 0; j < 100; j++) {
//     temp.push(0);
//   }
//   arr.push(temp);
// }

// for (let i = 1; i <= num; i++) {
//   let [row, col] = input[i].split(" ").map((el) => Number(el));

//   for (let j = row; j < row + 10; j++) {
//     for (let k = col; k < col + 10; k++) {
//       arr[j][k] = 1;
//     }
//   }
// }

// let count = 0;

// for (let el of arr) {
//   for (let num of el) {
//     if (num === 1) count++;
//   }
// }
// console.log(count);

let fs = require("fs");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

function solution() {
  const whites = Array.from({ length: 100 }, () => Array(100).fill(0));
  const blacks = input
    .slice(1, Number(input[0]) + 1)
    .map((row) => row.split(" ").map(Number));
  let count = 0;
  for (const black of blacks) {
    for (let i = black[0]; i < black[0] + 10; i++) {
      for (let j = black[1]; j < black[1] + 10; j++) {
        if (whites[i][j] === 0) {
          count++;
        }
        whites[i][j] = 1;
      }
    }
  }
  console.log(count);
}

solution();
