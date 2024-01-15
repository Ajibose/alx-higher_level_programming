#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
