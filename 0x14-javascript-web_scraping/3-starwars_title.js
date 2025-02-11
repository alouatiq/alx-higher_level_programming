#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    console.log(body.title);
  } else {
    console.log(`Failed to get a valid response: ${response.statusCode}`);
  }
});
