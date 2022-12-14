#!/usr/bin/node
const process = require('process');

function factorial (num) {
  // If the number is less than 0, reject it.
  if (num < 0) {
    return -1;
  // If the number is 0, its factorial is 1.
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

if (!process.argv[2]) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
