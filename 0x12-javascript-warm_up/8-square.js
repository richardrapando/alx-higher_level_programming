#!/usr/bin/node
const argu = parseInt(process.argv[2]);
if (Number.isNaN(argu)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < argu; x++) {
    let row = '';
    for (let y = 0; y < argu; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
