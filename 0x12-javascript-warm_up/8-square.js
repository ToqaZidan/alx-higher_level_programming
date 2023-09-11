#!/usr/bin/node

/* Write a script that prints a square */

const args = process.argv;
if (args.length === 2 || isNaN(args[2])) {
  console.log('Missing size');
} else if (args.length === 3 && !isNaN(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('X'.repeat(parseInt(args[2])));
  }
}
