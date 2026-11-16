#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, body) => {
  if (err) {
    throw err;
  }
  const characters = JSON.parse(body).characters;
  const print = (i) => {
    if (i === characters.length) {
      return;
    }
    request(characters[i], (err, res, body) => {
      if (err) {
        throw err;
      }
      console.log(JSON.parse(body).name);
      print(i + 1);
    });
  };
  print(0);
});
