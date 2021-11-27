let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
}

function partOne(data) {
}

function partTwo(data) {
}

module.exports = { run, parseData, partOne, partTwo }
