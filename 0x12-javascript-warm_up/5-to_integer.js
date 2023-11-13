#!/usr/bin/node

args = process.argv;
myNum = Number(args[2]);
if (typeof myNum.isNaN) {
	console.log("Not a number");
} else {
	console.log(myNum);
}
