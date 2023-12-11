#!/usr/bin/node
if ((process.argv.length - 2 <= 1)) {
  console.log('0');
} else {
  const n = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  const secondBigNum = n.length >= 2 ? n[1] : 0;
  console.log(secondBigNum);
}
