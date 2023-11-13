#!/usr/bin/node

/* Write a script that printsarguments passed to it.
*/

const firstArg = process.argv[2];

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
