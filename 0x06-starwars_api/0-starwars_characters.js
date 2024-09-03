#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <SWAPI film ID>');
  process.exit(1);
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    // now to get the names in the same order
    const charactersPromises = characters.map(function (character) {
      return new Promise(function (resolve, reject) {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });
    Promise.all(charactersPromises).then(function (characters) {
      characters.forEach(function (character) {
        console.log(character);
      });
    }).catch(function (error) {
      console.error(error);
    });
  }
});
