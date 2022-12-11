#!/usr/bin/node
// import { argv } from 'node:process';
const process = require('process');

const args = process.argv;
let count = 0;
// print process.argv
args.forEach((val, index) => {
  count = index + 1;
});
if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
