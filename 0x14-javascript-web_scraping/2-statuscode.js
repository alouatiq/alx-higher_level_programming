#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  // Even if an error occurs (unlikely for valid HTTP responses),
  // we print the status code if available.
  if (response) {
    console.log(`code: ${response.statusCode}`);
  } else if (error) {
    // Fallback in case there's no response object.
    console.log(`code: ${error.code}`);
  }
});
