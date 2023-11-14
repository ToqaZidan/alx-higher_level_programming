#!/usr/bin/node

/* Write a content that concats 2 files. */

const fs = require('fs');
let content = '';

content = content.concat(fs.readFileSync(process.argv[2]));
// content = content.concat('\n');
content = content.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], content);
