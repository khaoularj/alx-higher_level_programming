#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map((x, y) => x * y);
console.log(map1);
