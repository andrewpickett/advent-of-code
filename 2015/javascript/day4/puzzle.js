let utils = require('../aoc_utils')
let data = require('./input')
let md5 = require('md5')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	return data.trim();
}

function findHash(data, numZeros) {
	let i = 1;
	while (true) {
		if (md5(data + i).startsWith('0'.repeat(numZeros))) {
			return i;
		}
		i++;
	}
}

function partOne(data) {
	return findHash(data, 5);
}

function partTwo(data) {
	return findHash(data, 6);
}

module.exports = { run, parseData, partOne, partTwo }
