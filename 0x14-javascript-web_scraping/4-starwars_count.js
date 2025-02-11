#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode}`);
    return;
  }
  let count = 0;
  // Use a regex to match URLs that end with /18 or /18/
  const wedgeRegex = /\/18\/?$/;
  for (const film of body.results) {
    for (const charUrl of film.characters) {
      if (wedgeRegex.test(charUrl)) {
        count++;
        break; // Once found in a film, move to the next film.
      }
    }
  }
  console.log(count);
});
