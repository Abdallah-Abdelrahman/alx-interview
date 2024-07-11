#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie:
 *
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 */
const { argv: { 2: movieID } } = process;
const request = require('request');

request(
  `https://swapi-api.alx-tools.com/api/films/${movieID}`,
  (err, _response, body) => {
    if (err) {
      console.error('Error fetching film:', err);
    } else {
      const chars = JSON.parse(body).characters;

      const promises = chars.map((url) => new Promise((resolve, reject) => {
        request(url, (err, resp, body) => {
          if (err) {
            reject(err);
            return;
          }
          resolve(JSON.parse(body).name);
        })
      }));

      Promise.all(promises)
        .then((names) => {
          names.forEach((name) => console.log(name));
        })
        .catch((err) => {
          console.error('Error fetching character:', err);
        });
    }
  }
);
