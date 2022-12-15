#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
// Use fs.readFile() method to read the file
const texto = fs.readFileSync(file, 'utf-8');
console.log(texto);
