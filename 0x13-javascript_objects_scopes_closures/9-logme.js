#!/usr/bin/node
let xargs = 0;

exports.logMe = function (item){
  console.log(xargs + ': ' + item);
  xargs++;
};
