#!/usr/bin/node
const argu = parseInt(process.argv[2]);
if (Number.isNaN(argu)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argu);
}
