#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const texto = process.argv[3];
// Use fs.writeFileSync() method to writer the file
fs.writeFileSync(file, texto, 'utf-8');
