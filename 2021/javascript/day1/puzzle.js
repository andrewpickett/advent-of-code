let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = [];
	data.trim().split('\n').forEach(line => {
		d.push(parseInt(line));
	});
	return d;
}

function partOne(data) {
	let count = 0;
	for (let i = 1; i < data.length; i++) {
		if (data[i] > data[i-1]) {
			count++;
		}
	}
	return count;
}

function partTwo(data) {
	let count = 0;
	for (let i = 3; i < data.length; i++) {
		if (data[i] + data[i-1] + data[i-2] > data[i-1] + data[i-2] + data[i-3]) {
			count++;
		}
	}
	return count;
}

module.exports = { run, parseData, partOne, partTwo }
