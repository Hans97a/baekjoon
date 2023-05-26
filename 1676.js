let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let num = parseInt(fs.readFileSync(filePath).toString());

let result = Math.floor(num / 5);
let result25 = Math.floor(num / 25);
let result125 = Math.floor(num / 125);

console.log(result + result25 + result125);
