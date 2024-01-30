#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const Id = 18;

request.get(url, (error, response, body) => {
  const details = JSON.parse(body).results;
  const movies = details.filter(movie =>
    movie.characters.some(character => character.endsWith(`/${Id}/`))
  );
  console.log(error || movies.length);
});
