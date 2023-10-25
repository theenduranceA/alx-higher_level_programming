#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie: */

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

if (!filmId) {
  console.error('3');
} else {
  request.get(url, (filmErr, filmRes, filmBody) => {
    if (filmErr) {
      console.error(filmErr);
    } else {
      const film = JSON.parse(filmBody);
      const characters = film.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (characterErr, characterRes, characterBody) => {
          if (characterErr) {
            console.error(characterErr);
          } else {
            const character = JSON.parse(characterBody);
            console.log(character.name);
          }
        });
      });
    }
  });
}
