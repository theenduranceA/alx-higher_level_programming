#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');
const filmId = process.argv[2];
const url = `http://swapi.api.alx-tools.com/api/films/${filmId}`;

request.get(url, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(data);
    console.log(filmData.title);
  }
});
