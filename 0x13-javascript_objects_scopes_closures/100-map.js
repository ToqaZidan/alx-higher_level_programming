#!/usr/bin/node

/* Import list from the file 100-data.js */

const list = require('./100-data').list;
const map1 = list.map((value, index) => value * index);

console.log(list);
console.log(map1);
