#!/usr/bin/node
/* Script that display the status code of a GET request. */

const request = require('request');

request({ method: 'GET', uri: process.argv[2], json: true }, (err, response, body) => {
  if (!err) {
    console.log('code: ' + response.statusCode);
  } else {
    console.log(err);
  }
});
