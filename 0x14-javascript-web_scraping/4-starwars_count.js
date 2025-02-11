#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200 && body.results) {
    const films = body.results;
    let count = 0;
    films.forEach((film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/18/`)) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.log(`Failed to get a valid response: ${response.statusCode}`);
  }
});
