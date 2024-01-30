#!/usr/bin/node
const fs = require('fs');
const PathFl = process.argv[2];
fs.readFile(PathFl, 'utf8', (error, data) => {
  console.log(error || data);
});
