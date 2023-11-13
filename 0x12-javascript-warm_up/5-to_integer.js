#!/usr/bin/node

args = process.argv;
myNum = Number(args[2]);
if (isNaN(myNum)) {
	console.log("Not a number");
} else {
	console.log(myNum);
}
