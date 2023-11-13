#!/usr/bin/node
const argu = process.argv;
if (argu.length <= 3) {
  console.log(0);
} else {
  const args = argu.map(Number)
    .slice(2, argu.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
