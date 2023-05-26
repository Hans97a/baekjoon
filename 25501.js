let fs = require("fs");

//process.platform === 'linux' ? '/dev/stdin' : './input.txt'

function recursion(s, l, r, cnt) {
  cnt.n++;
  if (l >= r) return 1;
  else if (s[l] != s[r]) return 0;
  else return recursion(s, l + 1, r - 1, cnt);
}

function isPalidrome(s, cnt) {
  return recursion(s, 0, s.length - 1, cnt);
}

let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i = 1; i <= Number(input[0]); i++) {
  let cnt = { n: 0 };
  console.log(isPalidrome(input[i].trim(), cnt), cnt.n);
}
// let fs = require("fs");

// function recursion(s, l, r, cnt) {
//   cnt.n++;
//   if (l >= r) return 1;
//   else if (s[l] != s[r]) return 0;
//   else return recursion(s, l + 1, r - 1, cnt);
// }

// function isPalidrome(s, cnt) {
//   return recursion(s, 0, s.length - 1, cnt);
// }

// let input = fs
//   .readFileSync(__dirname + "/input.txt")
//   .toString()
//   .trim()
//   .split("\n");

// for (let i = 1; i <= Number(input[0]); i++) {
//   let cnt = { n: 0 };
//   console.log(isPalidrome(input[i].trim(), cnt), cnt.n);
// }
