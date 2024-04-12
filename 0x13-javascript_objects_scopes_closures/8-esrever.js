#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  const array = [];
  for (let i = size - 1; i >= 0; i--) {
    array.push(list[i]);
  }
  return array;
};
