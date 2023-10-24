#!/usr/bin/env node
/* Script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (parseError) {
      process.exit(1);
    }
  } else {
    process.exit(1);
  }
});
