#!/usr/bin/node

/* Define a class Rectangle */

module.exports = class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0) {
      return;
    }
    this.width = width;
    this.height = height;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
