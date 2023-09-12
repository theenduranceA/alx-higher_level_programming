#!/usr/bin/node
const pSquare = require('./5-square');

/* Creates a  class Square that defines a square and inherits from Square of 5-square.js */

module.exports = class Square extends pSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
