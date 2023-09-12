#!/usr/bin/node

/* script that imports a dictionary of occurrences by user id  */

const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
console.log(newDict);
