#!/usr/bin/node

function add(a, b) {
  console.log(Number(a) + Number(b));
}

args = process.argv;
add(args[2], args[3]);
