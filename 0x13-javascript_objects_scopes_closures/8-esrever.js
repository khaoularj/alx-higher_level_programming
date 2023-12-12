#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    listRev.push(list[i]);
  }
  return listRev;
};
