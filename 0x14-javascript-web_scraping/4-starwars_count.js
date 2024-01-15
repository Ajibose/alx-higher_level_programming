#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    let i = 0;
    for (const element of JSON.parse(body).results) {
      const characters = element.characters;
      characters.forEach(ch => {
        if (ch.endsWith('18/')) {
          i++;
        }
      });
    }
    console.log(i);
  }
});
