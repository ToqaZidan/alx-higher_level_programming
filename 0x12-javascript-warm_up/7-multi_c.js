#!/usr/bin/node

/* Write a script that prints x times “C is fun”.
    * Where x is the first argument of the script
    * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
*/

const args = process.argv;
if (args.length === 2) {
  console.log('Missing number of occurrences');
} else if (args.length === 3 && !isNaN(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
}
