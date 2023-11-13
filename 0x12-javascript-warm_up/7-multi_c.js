#!/usr/bin/node

const args = process.argv;
const myNum = parseInt(args[2]);
let i = 0;

if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  while (i < myNum) {
    console.log('C is fun');
    i++;
  }
}
