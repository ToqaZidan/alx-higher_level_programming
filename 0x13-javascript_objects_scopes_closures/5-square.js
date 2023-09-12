#!/usr/bin/node

/* Define a class Square that inherits from Rectangle */

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  double () {
    super.double();
  }
};
