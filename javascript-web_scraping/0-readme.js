#!/usr/bin/node
const request = require('request');

request.readfile('cisfun', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
