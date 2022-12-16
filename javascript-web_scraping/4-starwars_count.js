#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let results = [];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).results;
    for (const dict of results) {
      for (const item of dict.characters) {
        if (item.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
