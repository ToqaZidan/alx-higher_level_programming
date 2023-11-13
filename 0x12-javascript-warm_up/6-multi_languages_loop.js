#!/usr/bin/node

/* Write a script that prints 3 lines.
    * The first line: “C is fun”
    * The second line: “Python is cool”
    * The third line: “JavaScript is amazing”
    */

const script = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let index = 0;
while (index < script.length) {
  console.log(script[index]);
  index++;
}
