#!/usr/bin/node
const process = require('process');

function add (a, b) {
  let sum = 0;
  sum = a + b;
  console.log(sum);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
