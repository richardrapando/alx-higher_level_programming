#!/usr/bin/node
exports.MeMo = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
