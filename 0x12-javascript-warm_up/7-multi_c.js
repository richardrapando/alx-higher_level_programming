#!/usr/bin/node
const argu = parseInt(process.argv[2]);
if (Number.isNaN(argu)) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < argu; x++) {
    console.log('C is fun');
  }
}
