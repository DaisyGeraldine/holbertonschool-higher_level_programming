#!/usr/bin/node
// import { argv } from 'node:process';
const process = require('process');

let validation = 0;
// validate if arg[2] is number
validation = parseInt(process.argv[2]);
if (validation > 0) {
  console.log(`My number: ${validation}`);
} else {
  console.log('Not a number');
}
