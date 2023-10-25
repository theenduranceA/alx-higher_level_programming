#!/usr/bin/node
/* Script that computes the number of tasks completed by user id. */

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('https://jsonplaceholder.typicode.com/todos');
} else {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      const counts = {};

      for (const item of data) {
        if (item.completed) {
          counts[item.userId] = (counts[item.userId] || 0) + 1;
        }
      }

      console.log(counts);
    }
  });
}
