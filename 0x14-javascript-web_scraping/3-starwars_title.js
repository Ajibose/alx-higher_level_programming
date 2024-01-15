#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode >= 200 && response.statusCode < 300) {
    const bodyJson = JSON.parse(body);
    console.log(bodyJson.title);
  } else {
    console.error('Error:', `HTTP Status Code: ${response.statusCode}`);
  }
});
