#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let resultList = [];
const taskCompletedxUser = {};
// let id = '1'
// let cont = 1;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultList = JSON.parse(body);
    let id = 1;
    let count = 0;
    for (const item of resultList) {
      if (item.userId !== id) {
        count = 0;
        id++;
      }
      if (item.completed === true) {
        count++;
        taskCompletedxUser[`${id}`] = count;
      }
    }
    console.log(taskCompletedxUser);
  }
});
