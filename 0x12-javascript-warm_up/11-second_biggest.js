#!/usr/bin/node

/* Write a script that prints the second biggest integer of the list passed as argument:
    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
*/

const args = process.argv;
const numbers = args.slice(2).map(Number);

if (numbers.length < 2) {
  console.log('0');
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
