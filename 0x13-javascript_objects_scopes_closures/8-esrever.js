#!/usr/bin/node

/* Function that returns the reversed version of a list */

exports.esrever = function (list) {
  const myList = [];
  for (const element of list) {
    myList.unshift(element);
  }
  return myList;
};
