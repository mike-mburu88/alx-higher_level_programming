#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let l = 0; l < x; l++) {
    theFunction();
  }
};
