#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const EpNum = process.argv[2];

request.get(url + EpNum, (error, response, body) => {
  const details = JSON.parse(body);
  console.log(error || details.title);
});
