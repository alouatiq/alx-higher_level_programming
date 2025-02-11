#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }
  let count = 0;
  const films = body.results;
  films.forEach((film) => {
    // Check if the film's characters include character with id "18"
    for (let charUrl of film.characters) {
      // Split URL by '/' and filter out empty strings
      const parts = charUrl.split('/').filter(Boolean);
      // Get the last segment which should be the id
      const id = parts[parts.length - 1];
      if (id === '18') {
        count++;
        break;  // Count this film once and move to the next film
      }
    }
  });
  console.log(count);
});
