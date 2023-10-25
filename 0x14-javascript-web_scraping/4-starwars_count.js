#!/usr/bin/node
/* Script that prints the number of movies where the character “Wedge Antilles” is present. */

const request = require('request');
const url = process.argv[2];
const castId = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(castId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
