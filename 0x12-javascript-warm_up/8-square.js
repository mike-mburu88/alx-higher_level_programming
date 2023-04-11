#!/usr/bin/node
const sqsize = Math.floor(Number(process.argv[2]));
if (isNaN(sqsize)) {
  console.log('Missing size');
} else {
  for (let s = 0; s < sqsize; s++) {
    let srow = '';
    for (let r = 0; r < sqsize; r++) srow += 'X';
    console.log(srow);
  }
}
