#!/usr/bin/node
/* Define a class Square that inherits from Square */

const FirstSquare = require('./5-square.js');

module.exports = class Square extends FirstSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
