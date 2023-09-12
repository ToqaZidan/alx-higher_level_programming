#!/usr/bin/node

/* Define a class Rectangle */

module.exports = class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || !width || !height || isNaN(width) || isNaN(height) ||
    width === undefined || height === undefined || width === null || height === null) {
      return;
    }
    this.width = width;
    this.height = height;
  }
};
