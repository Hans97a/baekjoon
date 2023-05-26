const { count } = require("console");
let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let [n, m] = fs.readFileSync(filePath).toString().split(" ").map(Number);

function Count(a, b) {
  let cnt = 0;
  while (a > 0) {
    a = Math.floor(a / b);
    cnt += a;
  }
  return cnt;
}

let count2 = Count(n, 2) - Count(n - m, 2) - Count(m, 2);
let count5 = Count(n, 5) - Count(n - m, 5) - Count(m, 5);

console.log(count2 > count5 ? count5 : count2);
