#!/usr/bin/node

const args = process.argv;
const myNum = parseInt(args[2]);

function factorial (myNum) {
  let result = 0;

  if (isNaN(myNum)) { return 1; }

  if (myNum === 1) { return 1; }

  result = myNum * factorial(myNum - 1);
  return result;
}

console.log(factorial(myNum));
