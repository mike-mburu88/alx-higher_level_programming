#!/usr/bin/node
const dict = require('./101-data').dict;

const vals = Object.values(dict);
const totalist = Object.entries(dict);
const newDictionary = {};
const valsUniq = [...new Set(vals)];
for (const m in valsUniq) {
  const list = [];
  for (const l in totalist) {
    if (totalist[l][1] === valsUniq[m]) {
      list.unshift(totalist[l][0]);
    }
   }
   newDictionary[valsUniq[m]] = list;
}
console.log(newDictionary);
