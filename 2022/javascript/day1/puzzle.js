let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function getCals(data) {
	let elfCals = [];
	let elfTotal = 0;
	data.forEach(x => {
		if (x === "") {
			elfCals.push(elfTotal);
			elfTotal = 0;
		} else {
			elfTotal += parseInt(x);
		}
	});
	return elfCals;
}

function parseData(data) {
	let d = data.trim();
	return d.split('\n');
}

function partOne(data) {
	return Math.max(...getCals(data));
}

function partTwo(data) {
	return getCals(data).sort((a, b) => b-a).slice(0, 3).reduce((p, a) => p+a);
}

module.exports = { run, parseData, partOne, partTwo }
