#!/bin/bash/node
/* Write a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:
*/

const args = process.argv;
if (args.length === 3 && !isNaN(args[2])) {
    console.log('My number: ' + parseInt(args[2]));
    }
    else if (args.length === 3 && isNaN(args[2])) {
        console.log('Not a number');
    }
    else {
        console.log('Not a number');
    }