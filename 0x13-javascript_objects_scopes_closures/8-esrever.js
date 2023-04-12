#!/usr/bin/node
exports.esrever = function (list){
  let l = list.length - 1;
  let m = 0;
  while ((l - m) > 0) {
    const size = list[l];
    list[l] = list[m];
    list[m] = size;
    m++;
    l--;
  }
  return list;
};
