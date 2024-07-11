#!/usr/bin/node

/**
 * script that prints all characters of a Star Wars movie:
 *
 * The first positional argument passed is the Movie ID.
 * - example: 3 = “Return of the Jedi”
 */
const request = require('request');
const { argv: { 2: movieID } } = process;

request(
  `https://swapi-api.alx-tools.com/api/films/${movieID}`,
  (err, _response, body) => {
    if (err) {
      console.error({ err });
      return;
    }

    const chars = JSON.parse(body).characters;

    const promises = chars.map((url) => new Promise((resolve, reject) => {
      request(url, (err, _resp, body) => {
        if (err) {
          reject(err);
          return;
        }
        resolve(JSON.parse(body).name);
      });
    }));

    Promise.all(promises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((err) => {
        console.error({ err });
      });
  }
);
