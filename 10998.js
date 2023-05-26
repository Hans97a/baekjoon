let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")


let numbers = input[1].split(" ").map(el=> Number(el))
let toFind = Number(input[2])
let count = 0;

for(let i of numbers){
    if(i === toFind){
        count++;
    }
}

console.log(count)


// let input = require("fs")
//   .readFileSync(__dirname+"/input.txt")
//   .toString()
//   .trim()
//   .split("\n")


// let numbers = input[1].split(" ").map(el=> Number(el))
// let toFind = Number(input[2])
// let count = 0;

// for(let i of numbers){
//     if(i === toFind){
//         count++;
//     }
// }

// console.log(count)

