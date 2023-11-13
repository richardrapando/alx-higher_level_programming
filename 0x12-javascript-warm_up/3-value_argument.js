#!/usr/bin/node
const argu = process.argv;
if (argu[2] !== undefined) {
  console.log(argu[2]);
} else {
  console.log('No argument');
}
