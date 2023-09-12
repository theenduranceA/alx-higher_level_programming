#!/usr/bin/node

/* Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence */

const dict = require('./101-data.js').dict;

const myDict = {};
for (const element in dict) {
  if (myDict[dict[element]] === undefined) {
    myDict[dict[element]] = [];
  }
  myDict[dict[element]].push(element);
}
console.log(myDict);
