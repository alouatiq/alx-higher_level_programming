#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, todos) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    const completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  } else {
    console.error(`Failed to get a valid response: ${response.statusCode}`);
  }
});
