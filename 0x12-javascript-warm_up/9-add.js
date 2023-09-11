#!/usr/bin/node

/* Write a script that prints the addition of 2 integers.
    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype: function add(a, b)
*/

function add (a, b) {
  return a + b;
}

const args = process.argv;
if (args.length === 4 && !isNaN(args[2]) && !isNaN(args[3])) {
  console.log(add(parseInt(args[2]), parseInt(args[3])));
} else {
  console.log('NaN');
}
