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
  const characters = film.characters;
  // Recursive function to fetch each character in order
  const fetchCharacter = (i) => {
    if (i >= characters.length) return;
    request(characters[i], { json: true }, (err, resp, character) => {
      if (err) {
        console.error(err);
      } else if (resp.statusCode === 200) {
        console.log(character.name);
      }
      // Fetch next character once the current one has been processed
      fetchCharacter(i + 1);
    });
  };
  fetchCharacter(0);
});
