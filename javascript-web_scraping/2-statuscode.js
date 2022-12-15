#!/usr/bin/node
const request = require('request');
const ruta = process.argv[2];

request.get(ruta, function (error, response, body) {
  if (response.statusCode === 200) {
  // console.log(body);
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
