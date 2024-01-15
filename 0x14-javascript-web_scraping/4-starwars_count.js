#!/usr/bin/node
const request = require('request');
const id = 18;

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let i = 0;
  const wedgeUrl = `https://swapi-api.alx-tools.com/api/people/${id}/`;

  for (const element of JSON.parse(body).results) {
    if (element.characters.includes(wedgeUrl)) {
      i++;
    }
  }
  console.log(i);
});
