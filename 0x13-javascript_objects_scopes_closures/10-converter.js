#!/usr/bin/node

exports.converter = function (base) {
  return function (numx) {
    return numx.toString(base);
  };
};
