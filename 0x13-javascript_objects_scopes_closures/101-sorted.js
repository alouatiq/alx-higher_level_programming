#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [user, count] of Object.entries(dict)) {
    if (!newDict[count]) {
        newDict[count] = [];
    }
    newDict[count].push(user);
}
console.log(newDict);
