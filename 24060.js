let fs = require("fs");

let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";

function merge(l, r) {
  let left = 0,
    right = 0;
  let merged = [];
  while (l.length > left && r.length > right) {
    if (l[left] < r[right]) merged.push(l[left++]);
    else merged.push(r[right++]);
    count++;
    if (count === k) result = merged[merged.length - 1];
  }
  while (l.length > left) {
    merged.push(l[left++]);
    count++;
    if (count === k) result = merged[merged.length - 1];
  }
  while (r.length > right) {
    merged.push(r[right++]);
    count++;
    if (count === k) result = merged[merged.length - 1];
  }

  return merged;
}

function divide(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  let mid = Math.ceil(arr.length / 2);
  let l = divide(arr.slice(0, mid));
  let r = divide(arr.slice(mid));
  return merge(l, r);
}

let input = fs.readFileSync(filePath).toString().trim().split("\n");
let [n, k] = input[0].split(" ").map(Number);
let nums = input[1].split(" ").map(Number);
let result,
  count = 0;

divide(nums);

console.log(!result ? -1 : result);
