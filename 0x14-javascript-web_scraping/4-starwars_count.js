#!/usr/bin/node
const request = require('request');

const url = process.argv[2]; // The API URL for films

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to get a valid response: ${response.statusCode}`);
    return;
  }
  const films = body.results;
  let count = 0;
  // Wedge Antilles has ID 18, so his URL is:
  const wedgeURL = 'https://swapi-api.alx-tools.com/api/people/18/';
  films.forEach(film => {
    if (film.characters.includes(wedgeURL)) {
      count++;
    }
  });
  console.log(count);
});
