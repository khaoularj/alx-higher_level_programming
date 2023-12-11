#!/usr/bin/node
if ((process.argv.length - 2 === 0) || (isNaN(process.argv[2]))) {
  console.log('Missing size');
} else {
  const n = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
