#!/usr/bin/node
const process = require('process');

if (parseInt(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    let text = '';
    for (let i = 0; i < process.argv[2]; i++) {
      text += 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
}
