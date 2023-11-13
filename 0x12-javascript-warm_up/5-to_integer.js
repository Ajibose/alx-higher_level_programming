#!/usr/bin/node

args = process.argv;
myNum = parseInt(args[2]);
if (isNaN(myNum)) {
	console.log("Not a number");
} else {
	console.log("My number: " + myNum);
}
