#!/usr/bin/node

const args = process.argv;
const strLen = args.length;

if (strLen < 3) {
  console.log('No argument');
} else if (strLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
