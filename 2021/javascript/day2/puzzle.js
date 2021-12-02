let utils = require('../aoc_utils')
let data = require('./input')

function run(part) {
	const d = parseData(data);
	return (part === 1) ? utils.runWithTimer(partOne, d) : utils.runWithTimer(partTwo, d);
}

function parseData(data) {
	let d = [];
	data.trim().split('\n').forEach(line => {
		d.push(line.split(' '));
	});
	return d;
}

function partOne(data) {
	let dist = 0;
	let depth = 0;
	for (const d of data) {
		switch (d[0]) {
			case 'forward':
				dist += parseInt(d[1]);
				break;
			case 'down':
				depth += parseInt(d[1]);
				break;
			case 'up':
				depth -= parseInt(d[1]);
				break;
		}
	}
	return dist * depth;
}

function partTwo(data) {
	let dist = 0;
	let depth = 0;
	let aim = 0;
	for (const d of data) {
		switch (d[0]) {
			case 'forward':
				dist += parseInt(d[1]);
				depth += aim * parseInt(d[1]);
				break;
			case 'down':
				aim += parseInt(d[1]);
				break;
			case 'up':
				aim -= parseInt(d[1]);
				break;
		}
	}
	return dist * depth;
}

module.exports = { run, parseData, partOne, partTwo }
