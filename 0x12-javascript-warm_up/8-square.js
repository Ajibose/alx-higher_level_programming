#!/usr/bin/node

const args = process.argv;
const myNum = parseInt(args[2]);
const letter = 'X'
let i = 0;

if (isNaN(myNum)) {
  console.log("Missing size");
} else {
  while (i < (myNum ** 2)) {
    console.log(letter + '\r');
    i++;
  }
}


