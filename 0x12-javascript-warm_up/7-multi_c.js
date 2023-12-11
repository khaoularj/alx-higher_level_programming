#!/usr/bin/node
if ((process.argv.length - 2 === 0) || (isNaN(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < n; i++) {
    console.log('C if fun');
  }
}
