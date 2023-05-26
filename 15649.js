let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let [n, m] = fs.readFileSync(filePath).toString().split(" ").map(Number);
let arr = [];

function recursive() {
  if (arr.length === m) {
    let line = "";
    for (let i = 0; i < arr.length; i++) line += `${arr[i]} `;
    console.log(line);
    return;
  }

  for (let i = 1; i <= n; i++) {
    if (!arr.includes(i)) {
      arr.push(i);
      recursive();
      arr.pop();
    }
  }
}

recursive();
