#!/usr/bin/node

/* Import list from the file 100-data.js */

const list = require('./100-data').list;

console.log(list);

const map1 = list.map((x) => x * list.indexOf(x));

console.log(map1);
