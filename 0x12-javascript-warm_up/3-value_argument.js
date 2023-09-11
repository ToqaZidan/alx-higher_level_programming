#!/usr/bin/node

/* Write a script that printsarguments passed to it.
*/

const args = process.argv;
if (args.length === 2) {
    console.log('No argument');
    } else if (args.length === 3) {
        console.log(args[2]);
    } else {
        console.log('Arguments found');
    }