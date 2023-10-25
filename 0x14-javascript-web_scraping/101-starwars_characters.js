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
      const characters = JSON.parse(filmBody).characters;
      fetchAndPrintCharacters(characters, 0);
    }
  });
}

function fetchAndPrintCharacters (characters, index) {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (characterErr, characterRes, characterBody) => {
    if (characterErr) {
      console.error(characterErr);
    } else {
      const character = JSON.parse(characterBody);
      console.log(character.name);
      fetchAndPrintCharacters(characters, index + 1);
    }
  });
}
