#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    reversedList[j] = list[i];
  }
  return reversedList;
};
