let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let input = fs.readFileSync(filePath).toString().trim().split("\n");
for (let i = 1; i < input.length; i++) {
  let [n, m] = input[i].split(" ").map(BigInt);
  console.log(comb(m, n) + "");
}

function fac(n) {
  if (n <= 1n) return 1n;
  return n * fac(n - 1n);
}

function comb(n, m) {
  return fac(n) / (fac(m) * fac(n - m));
}
