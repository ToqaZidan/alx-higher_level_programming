#!/usr/bin/node

/* Update this script by adding a new function
    incr that increments the integer value.
*/

const myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
    function incr() {
      myObject.value++;
    }
    myObject.incr = incr;
  
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);