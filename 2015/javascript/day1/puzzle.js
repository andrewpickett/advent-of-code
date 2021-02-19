let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	return data.trim();
}

function partOne(data) {
	return (data.match(/\(/g) || []).length - (data.match(/\)/g) || []).length;
}

function partTwo(data) {
	let curr_floor = 0
	for (const [i, e] of [...data].entries()) {
		curr_floor += e === '(' ? 1 : -1;
		if (curr_floor < 0) {
			return i + 1;
		}
	}
}

module.exports = { run, parseData, partOne, partTwo }
