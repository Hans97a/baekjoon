let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let [n, k] = fs.readFileSync(filePath).toString().trim().split(" ").map(BigInt);

function fac(a) {
  if (a > 1n) {
    return a * fac(a - 1n);
  } else {
    return 1n;
  }
}

console.log(parseInt((fac(n) / (fac(k) * fac(n - k))) % 10007n));
