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
    for (const item of resultList) {
      if (item.completed === true) {
        taskCompletedxUser[`${item.userId}`] = 0;
      }
    }
    for (const item of resultList) {
      if (item.completed === true) {
        taskCompletedxUser[`${item.userId}`] = taskCompletedxUser[`${item.userId}`] + 1;
      }
    }
    console.log(taskCompletedxUser);
  }
});
