#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const bodyJson = JSON.parse(body);
  const taskCount = {};
  bodyJson.forEach(ch => {
    if (ch.completed === true) {
      if (ch.userId in taskCount) {
        taskCount[ch.userId] += 1;
      } else {
        taskCount[ch.userId] = 1;
      }
    }
  });
  console.log(taskCount);
});
