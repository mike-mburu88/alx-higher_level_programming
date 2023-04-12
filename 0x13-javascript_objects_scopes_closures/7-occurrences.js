#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let xOccurences = 0;
  for (let m = 0; m < list.length; m++) {
    if (searchElement === list[m]) {
      xOccurences++;
    }
  }
  return xOccurences;
};
