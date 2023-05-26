let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [n, m] = input[0].split(" ").map((e) => Number(e));

for (let i = 1; i <= n; i++) {
  let a = input[i].split(' ');
  let b = input[i+n].split(' ');
  let arr = [];
    for (let j = 0; j<a.length; j++){
        arr.push(Number(a[j]) + Number(b[j]))
    }
    console.log(arr.join(' '))
}


// let input = require("fs")
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .trim()
//   .split("\n");

// let [n, m] = input[0].split(" ").map((e) => Number(e));

// for (let i = 1; i <= n; i++) {
//   let a = input[i].split(' ');
//   let b = input[i+n].split(' ');
//   let arr = [];
//     for (let j = 0; j<a.length; j++){
//         arr.push(Number(a[j]) + Number(b[j]))
//     }
//     console.log(arr.join(' '))
// }

