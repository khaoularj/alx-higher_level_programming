#!/usr/bin/node
const fs = require('fs');
const PathFl = process.argv[2];
const Content = process.argv[3];
fs.writeFile(PathFl, Content, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
