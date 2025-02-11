#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(filmUrl, { json: true }, (error, response, film) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }
  // For each character URL, make an independent request.
  film.characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (err, resp, character) => {
      if (err) {
        console.error(err);
        return;
      }
      if (resp.statusCode === 200) {
        console.log(character.name);
      }
    });
  });
});
