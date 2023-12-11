#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const res = number + 1;
  theFunction(res);
}
