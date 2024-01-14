#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];
fs.writeFile(filePath, stringWrite, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit();
  }
});
