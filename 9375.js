let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

let input = fs.readFileSync(filePath).toString().trim().split("\n");
let idx = 0;

for (let i = 0; i < parseInt(input[0]); i++) {
  let num = parseInt(input[++idx]);
  let dic = {};
  for (let j = 0; j < num; j++) {
    let line = input[++idx].trim().split(" ");
    if (dic[line[1]]) dic[line[1]].push(line[0]);
    else {
      dic[line[1]] = [];
      dic[line[1]].push(line[0]);
    }
  }
  let result = 1;
  for (let key of Object.keys(dic)) {
    result *= dic[key].length + 1;
  }
  console.log(result - 1);
}
