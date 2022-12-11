#!/usr/bin/node
const process = require('process');
const args = process.argv;
let count = 0;
const listArg = [];

for (let i = 0; i < args.length; i++) {
  count = count + 1;
  if (count > 2) {
    listArg.push(parseInt(process.argv[i]));
  }
}
const newList = listArg.sort(function (a, b) { return b - a; });

if (count <= 3) {
  console.log(0);
} else {
  console.log(newList[1]);
}
